from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})

def pages_login(request):
    return render(request, 'pages-login.html')

def pages_register(request):
    return render(request, 'pages-register.html')

def users_profile(request):
    return render(request, 'users-profile.html')
