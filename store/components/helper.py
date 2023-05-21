import random
from django.conf import settings
import os
from django.core.mail import send_mail
from store.models.cart import  Cart
from store.models.customer import  Customer
# from twilio.rest import Client

def generate_otp(length=6):
    otp = ""
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp




def OTPSender(email):
    subject = "OTP Verifcation"
    message = f"Your OTP is: {generate_otp()}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list,)


def CartItems(request):
    customer_email = request.session.get('email')
    customer = Customer.objects.get(email=customer_email)
    totalItem = Cart.objects.filter(customer=customer).count()
    return totalItem


