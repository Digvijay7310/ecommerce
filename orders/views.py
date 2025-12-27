from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .models import Order, OrderItem
from cart.models import CartItem
from accounts.models import Profile

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect('cart:cart')

    total = sum(item.total_price() for item in cart_items)

    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')  # from form textarea

        delivery_date = date.today() + timedelta(days=5)

        order = Order.objects.create(
            user=request.user,
            full_name=request.user.first_name,
            email=request.user.email,
            phone=phone,
            address=address,
            city=profile.city,
            pincode=profile.pincode,
            payment_method='COD',
            delivery_date=delivery_date,
            is_paid=False
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()
        return redirect('orders:order_success', order_id=order.id)

    return render(request, 'checkout.html', {
        'items': cart_items,
        'total': total,
        'profile': profile
    })


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = OrderItem.objects.filter(order=order)
    total = sum(item.price * item.quantity for item in items)
    return render(request, 'order_success.html', {
        'order': order,
        'items': items,
        'total': total
    })


@login_required
def order_detail(request, id):
    order = get_object_or_404(Order, id=id, user=request.user)
    items = OrderItem.objects.filter(order=order)
    total = sum(item.price * item.quantity for item in items)
    return render(request, 'order_detail.html', {
        'order': order,
        'items': items,
        'total': total
    })
