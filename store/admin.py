from django.contrib import admin
from store.models.product import  Product ,Category,Subcategory
from store.models.customer import  Customer
from store.models.cart import  Cart
from store.models.order import  Order



class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']


class AdminCategory(admin.ModelAdmin):
    list_display=['categoryName']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'subcategory':
            category_id = request.resolver_match.kwargs.get('object_id')
            if category_id:
                kwargs['queryset'] = Subcategory.objects.filter(category_id=category_id)
            else:
                kwargs['queryset'] = Subcategory.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class AdminSubcategory(admin.ModelAdmin):
    list_display=['category','subcategoryName']

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'subcategory':
    #         # Get the selected category from the request's POST data
    #         selected_category_id = request.POST.get('category')
    #         if selected_category_id:
    #             # Filter subcategories based on the selected category
    #             kwargs['queryset'] = Subcategory.objects.filter(category_id=selected_category_id)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)



class AdminOrder(admin.ModelAdmin):
    list_display=['customer' ,'product' ,'quantity' ,'price' ,'date']

# Register your models here.



admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Subcategory,AdminSubcategory)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Order,AdminOrder)