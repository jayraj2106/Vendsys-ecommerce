from api.serializers.payment_serializer import CreatePaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from orders.models import Order
from payments.models import Payment


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
            order=order,
            amount=order.total_price, 
            currency="INR",  
            status="PENDING"
        )
        