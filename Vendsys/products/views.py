from django.shortcuts import render
from .models import Product
from .models import Category

def product_list(request):
    category_id = request.GET.get('category')

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories
    })

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product': product})


