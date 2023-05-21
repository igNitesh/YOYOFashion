from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    Quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    image4 = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id=ids)

    @staticmethod
    def get_all_product_by_id(category_id):
        if category_id:
            return Product.objects.filter(category_id=category_id)
        else:
            return Product.objects.all()
