from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    address = models.TextField()
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('COD', 'Cash on Delivery'),
            ('CARD', 'Card'),
            ('UPI', 'UPI'),
        ],
        default='COD'
    )

    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.product.name