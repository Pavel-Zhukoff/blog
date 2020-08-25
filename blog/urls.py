from django.urls import path

from blog.views import BlogCreateView, BlogDetailView
from blog.views.blog import BlogListView
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/new', BlogCreateView.as_view(), name='blog-new'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]