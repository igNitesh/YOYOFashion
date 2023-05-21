import datetime
from django.views import View
from django.shortcuts import render , redirect
from store.models.customer import Customer
from store.models.cart import  Cart
from store.models.order import  Order
from django.db.models import Sum, F
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .helper import CartItems

class order(View):
    def get(self,request):
        email = request.session.get('email')
        if not email:
            return redirect('login') 
        else:
            customer = Customer.get_customer_by_email(email)
            cart_items = Cart.objects.filter(customer=customer)
            total = cart_items.aggregate(total_price=Sum(F('product__price') * F('quantity')))['total_price']
        
        Total_number_product = CartItems(request)

            
        context ={
            'user_address' : customer,
            'carts'  : cart_items,
            'Totalcost' : total,
            'Total'      : Total_number_product,

            }
        return render(request,template_name='order.html',context=context)
    def post(self, request):
        email = request.session.get('email')
        customer = Customer.get_customer_by_email(email)
        cart_items = Cart.objects.filter(customer=customer)

        if not cart_items:
            return render(request, template_name='order.html', context={'message': 'Cart does not exist'})

        total_cost = cart_items.aggregate(total_price=Sum(F('product__price') * F('quantity')))['total_price']

        # Create the order
        order = Order(
            customer=customer,
            product = cart_items.first().product,
            quantity=cart_items.first().quantity,
            price=total_cost,
            date=datetime.datetime.today(),
            status=False
        )
        order.save()

        # Clear the cart items
        cart_items.delete()
        print("Order sucessful......")
        return redirect('homepage')

# def send_order_confirmation_email(customer_email, order_id):
#     subject = "Order Confirmation"
#     message = render_to_string('order_confirmation_email.html', {
#         'customer_email': customer_email,
#         'order_number': order_number,
#         'items_ordered': items_ordered,
#         'quantities': quantities,
#         'subtotal': subtotal,
#         'shipping': shipping,
#         'tax': tax,
#         'total': total,
#         'shipping_address': shipping_address,
#         'order_tracking_link': order_tracking_link
#     })
#     send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [customer_email])
