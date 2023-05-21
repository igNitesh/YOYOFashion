from django.db import models
from .product import Product
from .customer import Customer



class Cart(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def add_to_cart(self):
        self.save()

    @staticmethod
    def get_cart_by_customer_email(customer_email):
        return Cart.objects.filter(customer__email=customer_email)



    