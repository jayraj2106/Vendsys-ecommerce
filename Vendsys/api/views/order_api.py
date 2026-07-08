from orders.models import Order
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.serializers.order_serializer import (
    OrderListSerializer,
    OrderDetailSerializer
)


class OrderViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user) \
            .prefetch_related('items__product') \
            .order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer   
        return OrderDetailSerializer     