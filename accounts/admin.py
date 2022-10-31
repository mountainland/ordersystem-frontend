from django.contrib import admin

# Register your models here.
class SignupCodesAdmin(admin.ModelAdmin):
    list_display = ('',)

admin.site.register(SignupCode, SignupCodesAdmin)
