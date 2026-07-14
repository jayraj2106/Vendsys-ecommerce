from rest_framework import serializers 
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductFilterSerializer(serializers.Serializer):
    category = serializers.IntegerField(required=False)
    min_price = serializers.FloatField(required=False)
    max_price = serializers.FloatField(required=False)