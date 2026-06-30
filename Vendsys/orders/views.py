from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Order,OrderItem

def place_order(request):
    if request.method != "POST":
        return redirect("product_list")
     
    cart = request.session.get('cart', {})

    if not cart:
        messages.warning(request, "Your cart is empty")
        return redirect("product_list")

    total_price = 0

    for product_id, item in cart.items():
        pass  # next step

    return redirect("cart_view")  # temporary
