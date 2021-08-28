from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    ph_no = models.CharField(max_length=10)


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    qty = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, default=None,help_text='select None' )

