from products.models import Product
from api.serializers.product_serializers import ProductSerializer,ProductFilterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()     
    serializer_class = ProductSerializer
    http_method_names = ['get'] 
    #can add post for upload a product

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        queryset = super().get_queryset()

        # validate query params
        filter_serializer = ProductFilterSerializer(data=self.request.GET)
        filter_serializer.is_valid(raise_exception=True)
        data = filter_serializer.validated_data

        # apply filters
        if "category" in data:
            queryset = queryset.filter(category_id=data["category"])

        if "min_price" in data:
            queryset = queryset.filter(price__gte=data["min_price"])

        if "max_price" in data:
            queryset = queryset.filter(price__lte=data["max_price"])

        return queryset

