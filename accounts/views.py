from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

from django.contrib.auth.models import User
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

user.last_name = 'Lennon'
user.save()

def signup_view(request):
    if(request.POST):
        signup_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        signup_code = login_data.get("signup_code")
        print(user_type, username, password)
        return HttpResponse("This is a post request")
    else:
        return render(request, "base.html")