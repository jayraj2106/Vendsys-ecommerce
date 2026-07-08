from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product

def get_cart_products(cart):
    product_ids = list(cart.keys())  # get all ids

    products = Product.objects.filter(id__in=product_ids)

    product_map = {}

    for product in products:
        product_map[str(product.id)] = product

    return product_map

def calculate_cart(cart, product_map):
    total = 0
    count = 0

    for pid, item in cart.items():
        quantity = item["quantity"]
        product = product_map.get(pid)

        if product:
            total += product.price * quantity
            count += quantity

    return total, count




@api_view(['GET'])
def cart_view_api(request):
    cart = request.session.get('cart', {})
    product_map = get_cart_products(cart)
    cart_data = []

    for product_id, item in cart.items():
        product = product_map.get(product_id)

        if not product:
            continue  # Skip if product not found

        quantity = item['quantity']  

        cart_data.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": quantity,
            "total": product.price * quantity
        })

    return Response(cart_data)



@api_view(['POST'])
def add_to_cart_api(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1 #increase quantity
    else:
        cart[str(product_id)] = {"quantity": 1} #add 

    request.session["cart"] = cart  # Save  
 
    product_map = get_cart_products(cart)
    total, count = calculate_cart(cart, product_map)


    return Response({
        "success": True,
        "quantity": cart[str(product_id)]["quantity"],
        "count": count,
        "cart_total": total
    })


@api_view(['POST'])
def increase_quantity_api(request, product_id):
    cart = request.session.get("cart", {})

    product_map = get_cart_products(cart)
    product = product_map.get(str(product_id))

    if not product:
        return Response({"error": "Product not found"}, status=404)

    if str(product_id) not in cart:
        return Response({"error": "Product not in cart"}, status=400)

    cart[str(product_id)]["quantity"] += 1
    request.session["cart"] = cart
    
    product_map = get_cart_products(cart)

    quantity = cart[str(product_id)]["quantity"]
    item_total = product.price * quantity

    # cart total and cart_count
    total, count = calculate_cart(cart, product_map)

    return Response({
        "quantity": quantity,
        "item_total": item_total,
        "cart_total": total,
        "count" : count,

    })


@api_view(['POST'])
def decrease_quantity_api(request, product_id):
    cart = request.session.get("cart", {})

    product_map = get_cart_products(cart)
    product = product_map.get(str(product_id))

    if not product:
        return Response({"error": "Product not found"}, status=404)

    if str(product_id) not in cart:
        return Response({"error": "Product not in cart"}, status=400)


   
    cart[str(product_id)]["quantity"] -= 1

    if cart[str(product_id)]["quantity"] <= 0:
        del cart[str(product_id)]
        request.session["cart"] = cart

        product_map = get_cart_products(cart) 
        total, count = calculate_cart(cart, product_map)

        return Response({
            "removed": True,
            "cart_total": total,
            "count" : count
        })


    quantity = cart[str(product_id)]["quantity"]
    item_total = product.price * quantity

    # Calculate cart total and count
    total, count = calculate_cart(cart, product_map)

    request.session["cart"] = cart

    product_map = get_cart_products(cart)

    return Response({
        "quantity" : cart[str(product_id)]["quantity"],
        "removed" : False,
        "item_total": item_total,
        "cart_total": total,
        "count" : count
})