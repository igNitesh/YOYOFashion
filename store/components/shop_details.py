from django.views import View
from django.contrib.auth.hashers import make_password ,check_password
from django.shortcuts import render , redirect
from store.models.product import  Product
from store.models.customer import  Customer
from store.models.cart import  Cart



class shop_details(View):
    def get(self,request):
        getData = request.GET
        product = getData.get('product')
        category = getData.get('category')
        print("product id = ",product)
        print("category id = ",category)
        product_details=Product.objects.get(id=product)
        product = Product.get_all_product_by_id(category)
        customer_email = request.session.get('email')
        customer = Customer.objects.get(email=customer_email)
        total = Cart.objects.filter(customer=customer).count()
        if customer_email:
            flag = True
        else:
            flag = False
        context = {
            'product_detail' : product_details,
            'products' : product,
            'Total' : total,
            'Flage'       : flag
        }
        return render(request,template_name='shop_details.html',context=context)

        
    def post(self, request):
    # Handling cart

        productid = request.POST.get('product')
        quantity = request.POST.get('quantity')
        customer_email = request.session.get('email')

        try:
            product = Product.objects.get(id=productid)
        except Product.DoesNotExist:
            # Handle the case when the product does not exist
            return render(request, template_name='shop_details.html', context={'error': 'Product not found'})

        if customer_email:
            try:
                customer = Customer.objects.get(email=customer_email)
            except Customer.DoesNotExist:
                # Handle the case when the customer does not exist
                return render(request, template_name='shop_details.html', context={'error': 'Customer not found'})

            cart = Cart(
                product=product,
                customer=customer,
                quantity=quantity
            )
            cart.add_to_cart()
            totalCartObject = Cart.objects.filter(customer=customer).count()
            context = {
                'Total': totalCartObject
            }
            return redirect('cart')
        else:
            # Handle the case when there is no customer email in session
            return render(request, template_name='shop_details.html', context={'error': 'No customer email in session'})