from django.views import View
from django.contrib.auth.hashers import make_password ,check_password
from django.shortcuts import render , redirect
from store.components.helper import CartItems
from store.models.product import  Product
from store.models.customer import  Customer
from store.models.cart import  Cart



class shop_details(View):
    def get(self,request):
        getData = request.GET
        product = getData.get('product')
        category = getData.get('category')
        
        if product:
            product_details=Product.objects.get(id=product)
        else:
            return redirect('shop')

        if category:
            product = Product.get_all_product_by_id(category)

        # total_cart_object = Cart.objects.filter(customer=customer_email).count()
        context = {
            'product_detail' : product_details,
            'products' : product,
            # 'Total' : total_cart_object,
        }
        return render(request,template_name='shop_details.html',context=context)

        
    def post(self, request):
    # Handling cart
        productid = request.POST.get('product')
        quantity = request.POST.get('quantity')
        customer_email = request.session.get('email')
        size = request.POST.get('size')
        colour = request.POST.get('color')

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
                quantity=quantity,
                colour=colour,
                size=size
            )
            cart.add_to_cart()
            total_item_in_cart  = CartItems(request)
            context = {
                'nuber_items_cart' : total_item_in_cart
            }
            return redirect('cart')
        else:
            return redirect('login')