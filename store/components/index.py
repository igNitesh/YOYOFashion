from django.shortcuts import redirect, render
from django.views import View
from store.models.cart import  Cart
from store.models.product import  Product ,Category
from store.models.customer import  Customer
from .helper import CartItems ,categories_and_subcategories


class index(View):
    def get(self,request):
        Total_number_product_incart = 0
        product = Product.objects.all()
        
        total_item_in_cart = CartItems(request)

        cat_and_subcat = categories_and_subcategories()
        context = {
            'products' : product,
            'nuber_items_cart' : total_item_in_cart,
            'categories' : cat_and_subcat.get('categories'),
            'subcategories' : cat_and_subcat.get('subcategories')
            }
        return render(request,template_name='index.html',context=context)
    def post(self,request):
        postData = request.POST

        return redirect('homepage')
