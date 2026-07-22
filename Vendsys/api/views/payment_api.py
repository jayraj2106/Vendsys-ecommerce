from api.serializers.payment_serializer import CreatePaymentSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from orders.models import Order
from payments.models import Payment

from django.utils import timezone
from datetime import timedelta

import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt



stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentAPIview(APIView):

    def post(self, request):
        serializer = CreatePaymentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        order_id = serializer.validated_data["order_id"]

        order = get_object_or_404(
            Order,
            id=order_id,
            user=request.user
            )

        if order.status != "pending":
            return Response(
                {"error": "Order is already paid or not eligible for payment"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        existing_payment = Payment.objects.filter(
            order=order,
            status="PENDING",
            created_at__gte=timezone.now() - timedelta(minutes=10)
        ).first()

        if existing_payment:
            return Response(
                {"error": "A payment is already in progress for this order"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        payment = Payment.objects.create(
            user=request.user,
            order=order,
            amount=order.total_price,  
            status="PENDING"
        )
        

        # create stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "inr",
                        "product_data": {
                            "name": f"Order #{order.id}",
                        },
                        "unit_amount": int(payment.amount * 100),
                    },
                    "quantity": 1,
                }
            ],
            metadata={
                "order_id": str(order.id),
            },
            success_url="https://vendsys-ecommerce.onrender.com/api/payments/payment-success/",
            cancel_url="https://vendsys-ecommerce.onrender.com/api/payments/payment-cancle/",
        )

    
        payment.stripe_session_id = checkout_session.id
        payment.save()


        return Response(
            {
                "checkout_url": checkout_session.url
            },
            status=status.HTTP_200_OK
        )
    


@api_view(["GET"])
def payment_success(request):
    return Response({
        "status": "success",
        "message": "Payment completed",
    })

@api_view(["GET"])
def payment_cancel(request):
    return Response({
        "status": "cancle",
        "message": "Payment incompleted",
    })

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    
    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            endpoint_secret
        )

        event_type = event["type"]
        
        print("WEBHOOK HIT:", event_type)

        if event_type == "checkout.session.completed":
            session = event["data"]["object"]

            stripe_session_id = session["id"]
            payment_status = session["payment_status"]

            payment_intent = session["payment_intent"]

            try:
                payment = Payment.objects.get(stripe_session_id=stripe_session_id)

            except Payment.DoesNotExist:
                print("Payment not found")
                return JsonResponse({"error": "Payment not found"}, status=404)

            
            if payment_status == "paid":
                payment = Payment.objects.get(stripe_session_id=stripe_session_id)
                
                order_id = session.metadata.get("order_id")
                order = Order.objects.get(id=order_id)

                payment.stripe_payment_intent = payment_intent
                payment.status = "SUCCESS"
                payment.save()

                # update related order
                order = payment.order
                order.status = "paid"
                order.save()

        print("Payment and Order updated successfully")

    except ValueError:
        return JsonResponse({"error": "Invalid payload"}, status=400)
    
    except stripe.error.SignatureVerificationError:
        return JsonResponse({"error": "Invalid signature"}, status=400)

    return JsonResponse({"status": "success"})