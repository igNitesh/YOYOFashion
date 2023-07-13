import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from store.models.cart import  Cart
from store.models.product import  Product ,Category,Subcategory
from store.models.customer import  Customer
from .helper import CartItems ,categories_and_subcategories
from store.forms.form import *


class shop(View):
    def get(self,request,filter_slug = None):
        cat_and_subcat = categories_and_subcategories()
        products = Product.objects.all()
        

        # recive from client 
        colours = request.GET.get('colour')
        sizes = request.GET.get('size')
        price = request.GET.get('price')

        print(colours,sizes,price)
        
        if filter_slug: #by category and subcatogory
            if('-' in filter_slug):
                sub_category = filter_slug.split('-')[1]
                sub_category = Subcategory.objects.filter(subcategoryName = sub_category).first()
                products = products.filter(subcategory__exact=sub_category)
            else:
                category = Category.objects.filter(categoryName=filter_slug.upper()).first()
                if category:
                    products = products.filter(category=category)
                else:
                    products = Product.objects.none()
        
        if colours:
            if 'colours-all' == colours:
                products = Product.objects.all()
            else:
                products = Product.objects.filter(colour = colours)
            
        if sizes:
            if 'sizes-all' == sizes:
                products = Product.objects.all()
            products = Product.objects.filter(size__contains='M')
        
        if price:
            if 'price-all' == price:
                products = Product.objects.all()
            else:
                price_chart = {'price-1':[0,200],
                        'price-2':[200,400],
                        'price-3':[400,600],
                        'price-4':[600,1000],
                        'price-5':[1000,2000],
                        }
                price_range = price_chart.get(price)
                products = products.filter(price__gte=price_range[0],price__lte=price_range[1])
                
        total_item_in_cart = CartItems(request)
        print("cart::::::::: ",total_item_in_cart)
        context = {
            'products' : products,
            'categories' : cat_and_subcat.get('categories'),
            'subcategories' : cat_and_subcat.get('subcategories'),
            'nuber_items_cart' : total_item_in_cart
        }
        return render(request,template_name='shop.html',context=context)
    

