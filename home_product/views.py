from django.shortcuts import render
from .models import Product
# Create your views here.


def home(request):
    products = Product.objects
    return render(request, 'home_product/home.html', {'products': products})