from django.contrib import admin
from django import forms
from .models import Product, Order, Payment_method

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','name', 'description', 'price','created', 'last_updated',]
    readonly_fields = ['slug', 'created', 'last_updated',]

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_1','count_1','product_2','count_2','product_3','count_3','cost','order_by', 'name','address', 'postcode', 'city', 'delivered', 'delivered_on', 'created', 'last_updated', 'information', 'payment_method']
    readonly_fields = ['slug','order_by', 'created', 'last_updated']

admin.site.register(Order, OrderAdmin)