from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_archived=False)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(categories=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})
