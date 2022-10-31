from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from .models import Code

def SignUp(request):
    if (request.POST):
        signup_data = request.POST.dict()
        username = signup_data.get("username")
        password = signup_data.get("password")
        signup_code = signup_data.get("signup_code")
        if Code.objects.filter(code=signup_code).exists():
            user = User.objects.create_user(username, 'NOTAMAIL@MAIL.COM', password)
            user.save()
        return reverse_lazy('login')
    else:
        return render(request, 'registration/signup.html')