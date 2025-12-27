from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from cart.models import CartItem
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()[:8]

    cart_items = []
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)

    return render(request, 'home.html', {
        'products': products,
        'cart_items': cart_items,
    })

def product_search(request):
    query = request.GET.get('q', '').strip()

    products = []
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) 
        )

    return render(request, 'search.html', {
        'products': products,
        'query': query
        })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    cart_quantity = 0
    if request.user.is_authenticated:
        item = CartItem.objects.filter(user=request.user, product=product).first()
        if item:
            cart_quantity = item.quantity

    return render(request, 'product_detail.html', {'product': product})



    item = get_object_or_404(CartItem, id=id, user=request.user)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER', 'cart'))