from django.contrib import admin
from django import forms
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'description', 'price','created', 'last_updated',]
    readonly_fields = ['slug', 'created', 'last_updated',]

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','count','cost','order_by', 'name','address', 'postcode', 'city', 'delivered', 'delivered_on', 'created', 'last_updated', 'information']
    readonly_fields = ['slug','order_by', 'created', 'last_updated', 'payment_method']

admin.site.register(Order, OrderAdmin)