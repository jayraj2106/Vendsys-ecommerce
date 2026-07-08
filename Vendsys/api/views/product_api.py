from rest_framework.decorators import api_view
from products.models import Product
from api.serializers.product_serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet


# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)  

# @api_view(['GET'])
# def product_detail_api(request, id):
#     product = get_object_or_404(Product, id=id)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)  

class ProductViewSet(ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get'] #can add post for upload a product

