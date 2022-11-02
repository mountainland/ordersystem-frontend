from django.contrib import admin

from .models import Payment_method

class Payment_methodAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_name', 'info']

admin.site.register(Payment_method, Payment_methodAdmin)