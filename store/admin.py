from django.contrib import admin
from store.models.product import  Product ,Category
from store.models.customer import  Customer
from store.models.cart import  Cart
from store.models.order import  Order



class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']


class AdminCategory(admin.ModelAdmin):
    list_display=['name']


class AdminOrder(admin.ModelAdmin):
    list_display=['customer' ,'product' ,'quantity' ,'price' ,'date']

# Register your models here.



admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Order,AdminOrder)