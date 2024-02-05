from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product

def index(request):
    user = 'prince'
    products_number = 4
    products = Product.objects.all().order_by('-id')[:2]
    return render(request, 'products/home.html', {
        'name': user,
        'products_number': products_number,
        'products': products
    })

def signup(request):
    return render(request, 'products/signup.html' )

def product_cat(request, product):
    if product in ['suit','dress', 'shirts', 'shoes']:
        return HttpResponse(f'Here is the list of our {product}')
    else:
        return HttpResponse(f'{product.capitalize()} page is not exist')
