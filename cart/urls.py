# cart/urls.py
from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove/<int:id>/', views.remove_item, name='remove_item'),
    path('checkout/', views.checkout, name='checkout')
]
