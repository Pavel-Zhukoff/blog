from django.contrib.auth import views

from blog.forms import UserLoginForm

class LoginCustomView(views.LoginView):
    template_name = 'views/login.jhtml'
    authentication_form = UserLoginForm

