from django.urls import path
from .views import add_to_cart, cart_view, remove_item, update_cart_item

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:id>', add_to_cart, name='add_to_cart'),
    path('remove/<int:id>', remove_item, name='remove_item'),
    path('update/<int:id>/<str:action>/', update_cart_item, name='update_cart_item'),

]
