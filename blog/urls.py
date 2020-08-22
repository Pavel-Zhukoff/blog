from django.urls import path
from .views import HomeView
from .views import LoginCustomView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginCustomView.as_view(), name='login'),
]