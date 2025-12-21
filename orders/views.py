from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .models import Order, OrderItem
from cart.models import CartItem

# Create your views here.
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if request.method == 'POST':
        delivery_date = date.today() + timedelta(days=3)

        order = Order.objects.create(
            user=  request.user,
            full_name = request.POST['full_name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            address = request.POST['address'],
            city=request.POST['city'],
            pincode=request.POST['pincode'],
            payment_method=request.POST['payment_method'],
            delivery_date=delivery_date,
            is_paid=True
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()
        return redirect('order:order_success')
        
    return render(request, 'checkout.html', {
          'user':request.user,
          'cart_items': cart_items
    })
    

def order_success(request):
    return render(request, 'order_success.html')