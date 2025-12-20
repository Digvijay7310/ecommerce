from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.models import CartItem

def home(request):
    products = Product.objects.all()[:8]

    cart_quantities = {}
    if request.user.is_authenticated:
        items = CartItem.objects.filter(user=request.user)
        for item in items:
            cart_quantities[item.product.id] = item.quantity  # <-- fixed here

    return render(request, 'home.html', {
        'products': products,
        'cart_quantities': cart_quantities,
    })

def product_search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})
