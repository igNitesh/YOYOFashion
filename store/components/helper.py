import random
from django.conf import settings
import os
from django.core.mail import send_mail
from store.models.cart import  Cart
from store.models.customer import  Customer
from store.models.product import  *
# from twilio.rest import Client

def categories_and_subcategories():
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return {
        'categories': categories,
        'subcategories': subcategories
    }


def CartItems(request):
    customer_email = request.session.get('email')
    
    if customer_email:
        customer = Customer.objects.get(email=customer_email)
        totalItem = Cart.objects.filter(customer=customer).count()
        return totalItem
    else:
        return 0



