from django.contrib import admin
from Api.models import Customer, Product


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'ph_no']


@admin.register(Product)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'qty', 'price', 'date',]
