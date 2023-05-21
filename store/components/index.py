from django.shortcuts import redirect, render
from django.views import View
from store.models.cart import  Cart
from store.models.product import  Product ,Category
from store.models.customer import  Customer
from .helper import CartItems


class index(View):
    def get(self,request):
        
        customer_email = request.session.get('email')
        if customer_email:
            product = Product.objects.all()
            CATEGORIES = Category.objects.all()
            Total_number_product = CartItems(request)
            context = {
                'products' : product,
                'categories': CATEGORIES,
                'Total'      : Total_number_product,
            }
            return render(request,template_name='index.html',context=context)
        else:
            return redirect('login')
    def post(self,request):
        postData = request.POST

        return redirect('homepage')
