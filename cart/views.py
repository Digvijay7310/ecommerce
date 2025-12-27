from django.shortcuts import render, redirect, get_object_or_404
from cart.models import CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def increase_quantity(request, id):
    item = get_object_or_404(CartItem, id=id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart:cart')

@login_required
def decrease_quantity(request, id):
    item = get_object_or_404(CartItem, id=id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart:cart')

@login_required
def remove_item(request, id):
    item = get_object_or_404(CartItem, id=id, user=request.user)
    item.delete()
    return redirect('cart:cart')

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})


@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)

    return render(request, 'checkout.html', {
        'items': items,
        'total': total
    })