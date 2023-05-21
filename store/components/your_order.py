from django.views import View
from django.shortcuts import render , redirect
from store.models.order import Order
from store.models.customer import Customer

class Your_orderView(View):
    def get(self, request):
        customer_email = request.session.get('email')
        customer = Customer.objects.get(email=customer_email)
        orders = Order.get_orders_by_customer(customer_email)
        context = {
            'orders': orders
        }
        return render(request, 'yourorder.html', context)
