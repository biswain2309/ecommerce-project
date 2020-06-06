from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def home(request):
    products = Product.objects
    return render(request, 'products/home.html',{'products':products})


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html',{'product':product})


@login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart,created = Cart.objects.get_or_create(user=request.user, active=True)
    cart.add_to_cart(product_id)
    return redirect('cart')