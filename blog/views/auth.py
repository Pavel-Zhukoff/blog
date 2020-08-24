from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import UserLoginForm, UserRegisterForm


class LoginCustomView(views.LoginView):
    template_name = 'views/login.jhtml'
    authentication_form = UserLoginForm

class RegisterCustomView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'views/register.jhtml'