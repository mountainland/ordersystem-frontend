from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic
from .models import Code
from django.shortcuts import render
from django.shortcuts import redirect

USERMODEL = get_user_model()

def SignUp(request):
    if (request.POST):
        signup_data = request.POST
        username1 = signup_data["username"]
        password1 = signup_data["password1"]
        password2 = signup_data["password2"]
        if password1 == password2:
            password = password1
        else:
            return render(request, 'registration/signup.html')
        signup_code = signup_data["signup_code"]
        if Code.objects.filter(code=signup_code, used=False).exists():
            USERMODEL.objects.create_user(username=username1, password=password)
            code = Code.objects.get(code=signup_code)
            code.used = True
            code.save()
        return redirect('Product_order_create')
    else:
        return render(request, 'registration/signup.html')