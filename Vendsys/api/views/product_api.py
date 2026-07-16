from products.models import Product
from api.serializers.product_serializers import ProductSerializer,ProductFilterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.response import Response


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()     
    serializer_class = ProductSerializer
    http_method_names = ['get'] 


    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price']


    def get_queryset(self):
        queryset = super().get_queryset()

        filter_serializer = ProductFilterSerializer(data=self.request.GET)
        filter_serializer.is_valid(raise_exception=True)
        data = filter_serializer.validated_data

        if "category" in data:
            queryset = queryset.filter(category_id=data["category"])

        if "min_price" in data:
            queryset = queryset.filter(price__gte=data["min_price"])

        if "max_price" in data:
            queryset = queryset.filter(price__lte=data["max_price"])

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        queryset = self.filter_queryset(queryset)

        filter_serializer = ProductFilterSerializer(data=request.GET)
        filter_serializer.is_valid(raise_exception=True)
        data = filter_serializer.validated_data

        page = data.get("page", 1)
        page_size = data.get("page_size", 10)

        total_items = queryset.count()

        start = (page - 1) * page_size
        end = start + page_size

        queryset = queryset[start:end]

        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": (total_items + page_size - 1) // page_size,
            "results": serializer.data,
        })