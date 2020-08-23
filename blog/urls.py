from django.urls import path

from django.contrib.auth.views import LogoutView

from .views import HomeView
from .views import LoginCustomView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginCustomView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]