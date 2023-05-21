from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Customer(AbstractBaseUser):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    street = models.CharField(max_length=100,default="")
    city = models.CharField(max_length=100,default="")
    state = models.CharField(max_length=100,default="")
    country = models.CharField(max_length=100,default="")
    postal_code = models.CharField(max_length=20,default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.email

    def register(self):
        self.save()

    def isExists(self):
        return Customer.objects.filter(email=self.email).exists()

    @staticmethod
    def get_customer_by_email(email):
        return Customer.objects.filter(email=email).first()


