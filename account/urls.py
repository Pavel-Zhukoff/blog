from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import LoginCustomView, RegisterCustomView

urlpatterns = [
    path('login/', LoginCustomView.as_view(extra_context={'title': 'Вход'}), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterCustomView.as_view(extra_context={'title': 'Регитрация'}), name='register'),]