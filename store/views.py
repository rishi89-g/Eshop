from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product

# Create your views here.
def index(request):
    Prod = Product.get_all_product()
    return render (request, 'index.html', {'products': Prod})