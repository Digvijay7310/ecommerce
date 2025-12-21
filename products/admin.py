from django.contrib import admin
from .models import Product, Category, ProductImage

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 6
    max_num = 10


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'price', 'quantity', 'category')



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)