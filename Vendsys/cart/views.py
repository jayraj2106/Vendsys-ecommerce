from django.shortcuts import redirect, render
from products.models import Product

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1  #increase quantity
    else:
        cart[str(product_id)] = {"quantity": 1} #add 

    request.session["cart"] = cart  # Save   
    return redirect("product_list")  


def cart_view(request):
    cart = request.session.get("cart", {})
    product_ids = cart.keys()

    products = Product.objects.filter(id__in=product_ids)

    cart_items = []
    total = 0

    for product in products:
        quantity = cart[str(product.id)]["quantity"]
        total_price = product.price * quantity
        total += total_price

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "total_price": total_price
        })

    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total": total
    })
    
def decrease_quantity(request, product_id):
    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] -= 1

        if cart[str(product_id)]["quantity"] <= 0:
            del cart[str(product_id)]

    request.session["cart"] = cart
    return redirect("cart_view")

def increase_quantity(request, product_id):
    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1  # Increase quantity

    request.session["cart"] = cart  # Save the updated cart
    return redirect("cart_view")  # Redirect to the cart view
  