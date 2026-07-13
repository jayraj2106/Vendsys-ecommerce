from products.models import Product
from orders.models import Order,OrderItem
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.serializers.order_serializer import (
    OrderListSerializer,
    OrderDetailSerializer,
    OrderCreateSerializer
)
from decimal import Decimal
from rest_framework.exceptions import ValidationError
from django.db import transaction 

class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user) \
            .prefetch_related('items__product') \
            .order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        elif self.action == 'create':
            return OrderCreateSerializer   
        return OrderDetailSerializer 
    

    @transaction.atomic  #prevent halft created order if error 
    def perform_create(self, serializer):
        request = self.request
        user = request.user

        cart = request.session.get('cart', {})

        if not cart:
            raise ValidationError("Cart is empty")
             
        total_price = Decimal('0.00')

        order = serializer.save(user=user, total_price=Decimal('0.00'))

        
        for product_id, item in cart.items():
            product = Product.objects.get(id=int(product_id))
            quantity = item['quantity']

            price = product.price * quantity

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )

            total_price += price
            
        
        order.total_price = total_price
        order.save()
         
        request.session['cart'] = {}


        

