from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.home import about
from .views.home import contact
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import Checkout
from .views.order import OrderView
from .middlewares.auth import auth_middleware
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view()),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('order', auth_middleware(OrderView.as_view()), name='order'),
]
