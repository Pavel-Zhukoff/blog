from django.urls import path

from blog.views import BlogCreateView, BlogIdDetailView
from blog.views.blog import BlogListView, BlogAuthorListView
from .views import HomeView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/new', BlogCreateView.as_view(), name='blog-new'),
    path('blog/<int:pk>/', BlogIdDetailView.as_view(), name='blog-detail'),
path('blog/<username>/', BlogAuthorListView.as_view(), name='blog-list-author'),
]


