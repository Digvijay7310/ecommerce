from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=7)

    def __str__(self):
        return self.user.username