from rest_framework import serializers


class CreatePaymentSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()