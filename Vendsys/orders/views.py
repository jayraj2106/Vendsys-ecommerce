from django.shortcuts import render,redirect
from products.models import Product
from .models import Order,OrderItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def place_order(request):
    if request.method != "POST":
        return redirect("product_list")
     
    cart = request.session.get('cart', {})

    if not cart:
        return redirect("product_list")

    total_price = 0

    for product_id, item in cart.items():
        product = Product.objects.get(id=int(product_id))  
        total_price += product.price * item["quantity"]

    order = Order.objects.create(
        user=request.user,
        total_price = total_price,
        status = 'pending',
        address = request.POST.get('address')
    )

    for product_id, item in cart.items():
        product = Product.objects.get(id=int(product_id))  

        
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item["quantity"],
            price=item["quantity"] * product.price,
        )

    request.session["cart"] = {}

    return redirect("product_list")


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
   
    return render(request, "orders/orders.html", {
        "orders": orders,
    })


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    items = order.items.select_related("product")

    return render(request, "orders/order_details.html", {
        "order": order,
        "items": items
    })