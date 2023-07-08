
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from ..models.product import Product
from ..models.category import Category
from ..models.customer import Customer
from django.views import View
from django.db.models import F
from django.shortcuts import render, redirect

# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')

        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1

                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart']=cart
        return redirect('homepage')
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            request.session['cat']=categoryID
        ATOZ = request.GET.get('ATOZ')
        ZTOA= request.GET.get('ZTOA')
        PriceLH=request.GET.get('PriceLH')
        PriceHL=request.GET.get('PriceHL')
        products = Product.objects.all()

        if categoryID:
            products = products.filter(category=categoryID)

        if ATOZ:
            products = products.order_by('name')
        if ZTOA:
            products = products.order_by('-name')
        if PriceLH:
            products = products.order_by('price')
        if PriceHL:
            products = products.order_by('-price')
        data = {}
        data['products'] = products
        data['categories'] = categories

        return render(request, 'index.html', data)









def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
