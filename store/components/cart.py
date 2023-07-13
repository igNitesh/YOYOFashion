from django.views import View
from django.contrib.auth.hashers import make_password ,check_password
from django.shortcuts import render , redirect
from store.models.customer import  Customer
from store.models.cart import  Cart
from .helper import CartItems

class cart(View):
    def get(self,request):
        customer_email = request.session.get('email')
        customer = Customer.objects.get(email=customer_email)
        cart = Cart.objects.filter(customer=customer)
        total_item_in_cart = CartItems(request)
        context = {
            'carts' : cart,
            'nuber_items_cart': total_item_in_cart,
        }
        return render(request,template_name='cart.html',context=context)
    def post(sefl,request):
        Ritem  = request.POST.get('remove')
        customer_email = request.session.get('email')
        customer = Customer.objects.get(email=customer_email)
        Cart.objects.filter(id=Ritem).delete()
        cart = Cart.objects.filter(customer=customer)
        Total_number_product = CartItems(request)


        context = {
            'carts' : cart,
            'Total'      : Total_number_product,

        }
        return render(request,template_name='cart.html',context=context)
    



        


