from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.hashers import make_password ,check_password
from store.models.customer import Customer
from .helper import CartItems ,categories_and_subcategories

class Address(View):
    def get(self,request):
        email = request.session.get('email')
        if not email:
            # Handle the case where email is not available in the session
            # You can redirect to a login page or display an error message
            return redirect('login') 
        else:
            customer = Customer.get_customer_by_email(email)

        cat_and_subcat = categories_and_subcategories()
        total_item_in_cart = CartItems(request)
        context = {
                    'user_address' : customer,
                    'categories' : cat_and_subcat.get('categories'),
                    'subcategories' : cat_and_subcat.get('subcategories'),
                    'nuber_items_cart' : total_item_in_cart,
                }
        return render(request,template_name='address.html' , context = context)

    def post(self, request):
        postData = request.POST
        street = postData.get('street')
        city = postData.get('city')
        state = postData.get('state')
        country = postData.get('country')
        postal_code = postData.get('postal_code')
        
        email = request.session.get('email')
        if not email:
            # Handle the case where email is not available in the session
            # You can redirect to a login page or display an error message
            return redirect('login')  # Assuming you have a 'login' URL defined
        
        customer, created = Customer.objects.get_or_create(email=email)
        
        customer.street = street
        customer.city = city
        customer.state = state
        customer.country = country
        customer.postal_code = postal_code
        customer.save()
        
        return redirect('address')


def edit_address(request):
    states = [
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal',
    'Chandigarh',
    'Delhi',
    ]
    cat_and_subcat = categories_and_subcategories()
    total_item_in_cart = CartItems(request)
    context = {
                "states" : states,
                'nuber_items_cart' : total_item_in_cart,
                'categories' : cat_and_subcat.get('categories'),
                'subcategories' : cat_and_subcat.get('subcategories')
                }


    return render(request,template_name='edit_address.html',context = context )
         