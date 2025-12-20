from django.shortcuts import redirect, get_object_or_404, render
from .models import CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url='/accounts/login/')
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    # Increment quantity if already exists
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    else:
        item.quantity = 1
        item.save()

    cart_count = CartItem.objects.filter(user=request.user).count()
    return JsonResponse({
        'success': True,
        'cart_count': cart_count,
        'product_quantity': item.quantity
    })

   
@login_required(login_url='/accounts/login/')
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)

    for item in items:
        item.total_price = item.product.price * item.quantity
    return render(request, 'cart.html', {'items': items})

@login_required
def update_cart_item(request, id, action):
    item = get_object_or_404(CartItem, id=id, user=request.user)
    if action == 'increase':
        item.quantity += 1
        item.save()
    elif action == 'decrease' and item.quantity > 1:
        item.quantity -= 1
        item.save()
    elif action == 'decrease' and item.quantity == 1:
        item.delete()
        return JsonResponse({'success': True, 'deleted': True})

    return JsonResponse({'success': True, 'quantity': item.quantity})



@login_required(login_url='/accounts/login/')
def remove_item(request, id):
    item = get_object_or_404(CartItem, id=id, user=request.user)
    item.delete()
    return redirect('cart')
