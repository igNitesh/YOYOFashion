from django.shortcuts import redirect, render
from django.views import View
from store.models.cart import  Cart
from store.models.product import  Product ,Category
from store.models.customer import  Customer
from .helper import CartItems
class shop(View):
    def get(self,request):
        CATEGORIES = Category.objects.all()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.get_all_product_by_id(categoryID)
        else:
            product = Product.get_all_products()

        Total_number_product = CartItems(request)


        context = {
            'products' : product,
            'categories': CATEGORIES,
            'Total'      : Total_number_product,
        }
        return render(request,template_name='shop.html',context=context)
    def post(self,request):
        postData = request.POST
        CategoryId = postData.get('category')
        product = Product.objects.filter(Category = CategoryId)
        return redirect('homepage')
