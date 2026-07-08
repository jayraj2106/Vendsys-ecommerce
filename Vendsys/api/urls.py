from django.urls import path
from api.views.product_api import ProductViewSet
from rest_framework.routers import DefaultRouter
from api.views.cart_api import (
    add_to_cart_api,
    cart_view_api, 
    increase_quantity_api, 
    decrease_quantity_api
    )                             
                              

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')


urlpatterns = [
    path('cart/', cart_view_api, name='cart_view_api'),
    path('cart/add/<int:product_id>/', add_to_cart_api, name='add_to_cart_api'),
    path('cart/increase/<int:product_id>/', increase_quantity_api, name='increase_quantity_api'),
    path('cart/decrease/<int:product_id>/', decrease_quantity_api, name='decrease_quantity_api'),
]

#products urls
urlpatterns += router.urls