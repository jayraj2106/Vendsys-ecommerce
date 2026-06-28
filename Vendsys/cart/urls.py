from . import views
from django.urls import path


urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_view, name='cart_view'),
    path("decrease/<int:product_id>/", views.decrease_quantity, name="decrease_quantity"),
    path("increase/<int:product_id>/", views.increase_quantity, name="increase_quantity")
]