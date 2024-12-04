from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from .models import Product, User, Cart, Order, CartItem, OrderItem
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone


# Create your views here.
def home(request):
    products = Product.objects.all()
    logged_in = request.session.get('logged_in', False)
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    print(user_id, username)

    context = {
        'logged_in': logged_in,
        'user_id': user_id,
        'username': username,
        'products': products
    }   
    return render(request, 'website/home.html', context)

def product(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    category = product.category

    similar_products = Product.objects.filter(category=category).exclude(id=id)
    context['similar_products'] = similar_products
    return render(request, 'website/product.html', context)

def login_page(request):
    return render(request, 'website/login.html')





def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request,user)
            request.session['logged_in'] = True
            request.session['user_id'] = user.id
            request.session['username'] = user.first_name
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login_page')
    else:
        return render(request, 'login.html')



#logout function
def logout(request):
    request.session['logged_in'] = False
    request.session['user_id'] = None
    request.session['username'] = None
    messages.success(request, 'You have been logged out')
    return redirect('home')

def login_page(request):
    return render(request, 'website/login.html')


#signup_page function
def signup_page(request):
    return render(request, 'website/register.html')

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup_page')
        
        user = User(first_name=first_name, last_name=last_name, email=email ,username=username)
        user.set_password(password)
        user.save()
        return redirect('login_page')
    else:
        messages.error(request, 'Invalid request')
        return redirect('signup_page')

def add_to_cart(request, id):
    status = request.session.get('logged_in', False)
    product_id = request.session.get('product_id')
    if not status:
        return HttpResponse("<script>alert('Please login to add to cart');window.location.href='/login_page';</script>")
    
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=id)

    # Check if the user has a cart
    cart = Cart.objects.get_or_create(user=user)
    cart = cart[0]

    # Check if the product is already in the cart
    cart_item = CartItem.objects.filter(cart=cart, product=product, processed=False)
    if cart_item.exists():
        # If multiple cart items exist for the same product, sum their quantities
        if cart_item.count() > 1:
            quantity = sum(item.quantity for item in cart_item)
            cart_item.delete()  # Delete duplicate items
            cart_item = CartItem(cart=cart, product=product, quantity=quantity)
        else:
            cart_item = cart_item.first()
            cart_item.quantity += 1
    else:
        cart_item = CartItem(cart=cart, product=product, quantity=1)
    
    cart_item.save()
    #return to referer
    messages.success(request, 'Product added to cart')
    return redirect(request.META.get('HTTP_REFERER', 'home'))


#carts function
def cart(request):
    status = request.session.get('logged_in', False)
    if not status:
        return HttpResponse("<script>alert('Please login to view cart');window.location.href='/login_page';</script>")
    
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    cart_items = CartItem.objects.filter(cart__user=user, processed=False)
    carts = Cart.objects.filter(user=user)

    context = {
        'cart_items': cart_items
    }
    
    return render(request, 'website/cart.html', context)

#delete from cart function
def remove_from_cart(request, id):
    status = request.session.get('logged_in', False)
    if not status:
        return HttpResponse("<script>alert('Please login to delete from cart');window.location.href='/login_page';</script>")
    
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    cart = Cart.objects.get(user=user)
    product = Product.objects.get(id=id)

    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    messages.success(request, 'Product removed from cart')
    return redirect('cart')

#view for checkout
def checkout(request):

    context = {
        'logged_in': request.session.get('logged_in', False),
        'user_id': request.session.get('user_id'),
        'username': request.session.get('username'),
    }
    user = User.objects.get(id=context['user_id'])
    cart = Cart.objects.get(user=user)
    carts = CartItem.objects.filter(cart=cart, processed=False)
    total = 0
    for cart in carts:
        total += cart.get_total_price()
    count = carts.count()

    context['total'] = total
    context['carts'] = carts
    context['count'] = count
    context['user'] = user
    if carts.exists():
        return render(request,'website/checkout.html', context)
    else:
        messages.warning(request, 'No cart items found for this cart')
        return redirect('cart')
#view  order
def account(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    context = {
        'user': user
    }
    return render(request, 'website/account.html',context)
#view and edit address
def address(request):
    return render(request, 'website/address.html')

def phone_number(request):
    return render(request, 'website/phonenumber.html')

def email(request):
    return render(request, 'website/email.html')

def password(request):
    return render(request, 'website/password.html')

def orders(request):
    user = User.objects.get(id=request.session.get('user_id'))
    orders = Order.objects.filter(user=user)
    order_items = OrderItem.objects.filter(order__in=orders)
    
    context = {
        'orders': orders,
        'order_items': order_items
    }   
    return render(request, 'website/my_orders.html', context)    

def add_order(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    cart = Cart.objects.get(user=user)
    carts = CartItem.objects.filter(cart=cart, processed=False)

    if not carts.exists():
        messages.warning(request, 'You dont have any items in your cart')
        return redirect('cart')

    total = 0
    for cart_item in carts:
        total += cart_item.get_total_price()
    order = Order(user=user, total_amount=total,order_date=timezone.now())
    order.save()
    for cart_item in carts:
        cart_item.processed = True
        cart_item.save()
        order_item = OrderItem(
            order=order,
            cart_item=cart_item,
            product=cart_item.product,
            quantity=cart_item.quantity,
            price=cart_item.get_total_price(),
        )
        order_item.save()
    messages.success(request, 'Order placed successfully')
    return redirect('orders')
