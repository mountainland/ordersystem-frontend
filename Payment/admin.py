from django.contrib import admin

from .models import PaymentMethod

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_name', 'info']

admin.site.register(PaymentMethod, PaymentMethodAdmin)