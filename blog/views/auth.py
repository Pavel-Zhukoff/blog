from django.contrib.auth import views

class LoginCustomView(views.LoginView):
    template_name = 'views/login.html'