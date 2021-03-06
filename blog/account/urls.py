from django.contrib.auth.views import LogoutView
from django.urls import path

from blog.account.views import LoginCustomView, RegisterCustomView

urlpatterns = [
    path('login/', LoginCustomView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterCustomView.as_view(), name='register'),]