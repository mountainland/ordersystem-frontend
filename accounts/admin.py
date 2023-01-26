from django.contrib import admin
from . models import Code

# Register your models here.


class CodesAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'code', 'used')


admin.site.register(Code, CodesAdmin)
