from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from ..models.product import Product
from ..models.category import Category
from ..models.customer import Customer
from django.views import View

class Signup(View):
    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "Enter your first name!"
        elif len(customer.first_name) < 4:
            error_message = "First name must be 4 or more characters long!"
        elif not customer.last_name:
            error_message = "Enter your last name!"
        elif len(customer.last_name) < 4:
            error_message = "Last name must be 4 or more characters long!"
        elif not customer.email:
            error_message = "Enter an email address!"
        elif not customer.phone:
            error_message = "Enter your phone number!"
        elif not customer.phone.isdigit():
            error_message = "Phone number should consist only of digits!"
        elif len(customer.phone) != 10:
            error_message = "Enter a valid phone number of 10 digits!"
        elif not customer.password:
            error_message = "Enter a password!"
        elif len(customer.password) < 6:
            error_message = "Password must be 6 or more characters long!"

        # checking if email id already exists in the database
        elif customer.isExists():
            error_message = "Account with this email ID already exists!"
        return error_message

    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # holding values for error
        value = {'first_name': first_name,
                 'last_name': last_name,
                 'phone': phone,
                 'email': email
                 }
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        # validation
        error_message = self.validateCustomer(customer)
        # saving
        if not error_message:
            # before registering customer, hash the password
            customer.password = make_password((customer.password))
            # register the customer if everything file till now and no error
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)