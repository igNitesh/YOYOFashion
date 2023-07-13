from django.views import View
from django.shortcuts import render , redirect
from store.models.order import Order
from store.models.customer import Customer
from .helper import CartItems ,categories_and_subcategories
class Your_orderView(View):
    def get(self, request):
        customer_email = request.session.get('email')
        customer = Customer.objects.get(email=customer_email)
        orders = Order.get_orders_by_customer(customer_email)
        cat_and_subcat = categories_and_subcategories()
        total_item_in_cart = CartItems(request)
        context = {
            'orders': orders,
            'nuber_items_cart' : total_item_in_cart,
            'categories' : cat_and_subcat.get('categories'),
            'subcategories' : cat_and_subcat.get('subcategories')
        }
        return render(request, 'yourorder.html', context)
