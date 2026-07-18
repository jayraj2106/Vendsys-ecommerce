from api.serializers.payment_serializer import CreatePaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from orders.models import Order
from payments.models import Payment

import stripe
from django.conf import settings


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
            status="PENDING"
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
            currency="INR",  
            status="PENDING"
        )
        

        # create stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "product_data": {
                            "name": f"Order #{order.id}",
                        },
                        "unit_amount": int(payment.amount * 100),
                    },
                    "quantity": 1,
                }
            ],
            success_url="http://localhost:3000/success",
            cancel_url="http://localhost:3000/cancel",
        )


        # save stripe data in payment
        payment.stripe_session_id = checkout_session.id
        payment.stripe_payment_intent = checkout_session.payment_intent
        payment.save()


        # return response
        return Response(
            {
                "checkout_url": checkout_session.url
            },
            status=status.HTTP_200_OK
        )