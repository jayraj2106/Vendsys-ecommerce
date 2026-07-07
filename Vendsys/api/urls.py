from django.urls import path
from api.views.product_api import product_list_api, product_detail_api
from api.views.cart_api import add_to_cart_api, cart_view_api, increase_quantity_api, decrease_quantity_api

urlpatterns = [
    path('products/', product_list_api, name='product_list_api'),
    path('products/<int:id>/', product_detail_api, name='product_detail_api'),
    path('cart_view/', cart_view_api, name='cart_view_api'),
    path('add_to_cart/<int:product_id>/', add_to_cart_api, name='add_to_cart_api'),
    path('increase_quantity/<int:product_id>/', increase_quantity_api, name='increase_quantity_api'),
    path('decrease_quantity/<int:product_id>/', decrease_quantity_api, name='decrease_quantity_api'),

]