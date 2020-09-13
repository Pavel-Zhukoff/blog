from django.contrib.auth import views
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.account.forms import UserLoginForm, UserRegisterForm


class LoginCustomView(UserPassesTestMixin, views.LoginView):
    template_name = 'views/accounts/login.jhtml'
    authentication_form = UserLoginForm

    login_url = reverse_lazy('home') # Устанавливаем login_url на /, чтобы редиректило на главную, если пользователь авторизован

    def get_context_data(self, **kwargs):
        context = super(LoginCustomView, self).get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    def test_func(self):
        return not self.request.user.is_authenticated

class RegisterCustomView(UserPassesTestMixin, generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'views/accounts/register.jhtml'

    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(RegisterCustomView, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def test_func(self):
        return not self.request.user.is_authenticated