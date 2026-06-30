from django.shortcuts import redirect, render
from products.models import Product
from django.http import JsonResponse


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1  #increase quantity
    else:
        cart[str(product_id)] = {"quantity": 1} #add 

    request.session["cart"] = cart  # Save  
 
    count = sum(item["quantity"] for item in cart.values())

    return JsonResponse({
        "success" : True,
        "message" : "Product added",
        "quantity" : cart[str(product_id)]["quantity"],
        "count" : count,
    })  

    
def decrease_quantity(request, product_id):
    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] -= 1

        if cart[str(product_id)]["quantity"] <= 0:
            del cart[str(product_id)]
            request.session["cart"] = cart

            count = sum(item["quantity"] for item in cart.values())

            total = 0
            for pid, item in cart.items():
                product = Product.objects.get(id=pid)
                total += product.price * item["quantity"]

            return JsonResponse({
                "removed": True,
                "cart_total": total,
                "count" : count
            })

    product = Product.objects.get(id=product_id)
    quantity = cart[str(product_id)]["quantity"]
    item_total = product.price * quantity

    # Calculate cart total
    total = 0
    for pid, item in cart.items():
        p = Product.objects.get(id=pid)
        total += p.price * item["quantity"]

    request.session["cart"] = cart

    count = sum(item["quantity"] for item in cart.values())

    return JsonResponse({
        "quantity" : cart[str(product_id)]["quantity"],
        "removed" : False,
        "item_total": item_total,
        "cart_total": total,
        "count" : count
})


def increase_quantity(request, product_id):
    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1  # Increase quantity


    request.session["cart"] = cart  # Save the updated cart

     # Calculate totals
    product = Product.objects.get(id=product_id)
    quantity = cart[str(product_id)]["quantity"]
    item_total = product.price * quantity

    # cart total
    total = 0
    for pid, item in cart.items():
        p = Product.objects.get(id=pid)
        total += p.price * item["quantity"]

    count = sum(item["quantity"] for item in cart.values())

    return JsonResponse({
        "quantity": quantity,
        "item_total": item_total,
        "cart_total": total,
        "count" : count,

    })
  


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
        "total": total,

    })

