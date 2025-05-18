from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/list.html', {'products': products})

