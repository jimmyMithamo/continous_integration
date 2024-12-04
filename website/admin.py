from django.contrib import admin

# Register your models here.
from. models import User, Product, Profile, Cart, CartItem, Order, OrderItem
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)



