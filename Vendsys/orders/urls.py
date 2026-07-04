from django.urls import path
from . import views


urlpatterns = [
    path('place-order/', views.place_order, name="place_order"),
    path('orders/', views.order_list, name="orders"),
    path("<int:order_id>/", views.order_detail, name="order_detail"),
]