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



# def OTPSender(mobilenumber):
#         account_sid = "AC0c2c1ed119553abb2cd147c07f4307eb"
#         auth_token = "45ac466fdc23c26e2f85bf5945402c90"
#         verify_sid = "VA5a3d44ea903aabdbe250494483672fa0"
#         verified_number = "+91"+mobilenumber

#         client = Client(account_sid, auth_token)

#         otp = generate_otp()


#         message = client.messages.create(
#                               body=f"Your OTP is: {otp}",
#                               from_="+9999999",
#                               to=verified_number
#                           )

#         print(message.sid)
#         return otp