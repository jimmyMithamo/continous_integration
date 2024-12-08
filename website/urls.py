from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>', views.product, name='product'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('cart', views.cart, name='cart'),
    path('login_page', views.login_page, name='login_page'),
    path('signup_page', views.signup_page, name='signup_page'),
    path('signup', views.signup, name='signup'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>', views.remove_from_cart, name='remove_from_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('account', views.account, name='account'),
    path('address',views.address, name='address'),
    path('phone_number',views.phone_number, name='phone_number'),
    path('email',views.email, name='email'),
    path('password',views.password, name='password'),
    path('order',views.orders, name='orders'),
    path('add_order',views.add_order, name='add_order'),
    path('upload_image',views.upload_image, name='upload_image'),
    path('profile_Image',views.profile_Image, name='profile_Image'),
    path('buy_now/<int:id>', views.buy_now, name='buy_now'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
