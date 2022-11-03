from django.contrib import admin

from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'short', 'delivery_date']

admin.site.register(City, CityAdmin)