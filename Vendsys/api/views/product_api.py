from products.models import Product
from api.serializers.product_serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get'] #can add post for upload a product

