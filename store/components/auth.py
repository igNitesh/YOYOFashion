from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore

class signup(View):
    def get(self, request):
        return render(request, template_name='signup.html')

    def post(self, request):
        postData = request.POST
        Name = postData.get('name')
        Phone = postData.get('phone')
        Email = postData.get('email')
        Password = postData.get('password')
        re_pass = postData.get('re_passward')
        print(Name, Phone, Email, Password)

        customer = Customer(name=Name, phone=Phone, email=Email, password=Password)

        if customer.isExists():
            error_message = 'User Address Already Registered..'
            context = {'error': error_message}
            return render(request, template_name='signup.html', context=context)

        if Password == re_pass:
            customer.password = make_password(customer.password)
            customer.register()
            # Create a session for the registered user
            request.session['email'] = customer.email
            request.session['phone'] = customer.phone
            return redirect('homepage')


class login(View):
    def get(self, request):
        return render(request, template_name='login.html')

    def post(self, request):
        postData = request.POST
        email = postData.get('email')
        Password = postData.get('password')
        customer = Customer.get_customer_by_email(email)

        if customer:
            flag = check_password(Password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_message = "Password is incorrect !!!"
                context = {'error': error_message}
                return render(request, template_name='login.html', context=context)

        else:
            error_message = "Email is invalid !!!"
            context = {'error': error_message}
            return render(request, template_name='login.html', context=context)


def logout(request):
    request.session.clear()
    return redirect('login')




    


    