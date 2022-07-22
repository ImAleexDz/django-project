from itertools import product
from django.shortcuts import render
from products.models import Products

# Create your views here.

def create_product(request):
    new_product = Products.objects.create(
        name = "Coca Cola 1l",
        price = 20,
        stock = 20
    )

    context = {
        'new_product': new_product
    }

    return render(request, 'products.html', context=context)

def list_products(request):
    products = Products.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products_list.html', context=context)
