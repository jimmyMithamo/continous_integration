from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
    
#model for product class
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    image = models.ImageField(upload_to='profile/', default='profile/default.jpg')

    def __str__(self):
        return self.user.username
        
#model for cart class
class Cart(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   
   def __str__(self):
        return f'Cart {self.id} - {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_total_price(self):
        return self.quantity * self.product.price

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('UNPAID', 'Unpaid'),
        ('In transit', 'In transit'),
        ('COMPLETED', 'Completed'),
        ('CANCELED', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default='PENDING')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.CharField(max_length=255, default="No address provided")

    def __str__(self):
        return f'Order {self.id} - {self.user.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'OrderItem {self.id} - {self.product.name}'

    def get_total_price(self):
        return self.quantity * self.price
    
#model for order class
