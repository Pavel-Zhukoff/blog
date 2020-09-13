from django.urls import path

from blog.blog import BlogCreateView, BlogIdDetailView, create_article, get_article, get_articles, update_article
from blog.blog import BlogListView, BlogAuthorListView
from .views import HomeView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/new', BlogCreateView.as_view(), name='blog-new'),
    path('blog/<int:pk>/', BlogIdDetailView.as_view(), name='blog-detail'),
    path('blog/<username>/', BlogAuthorListView.as_view(), name='blog-list-author'),
    path('article/', get_articles, name='article-list'),
    path('article/new', create_article, name='article-new'),
    path('article/update/<int:pk>', update_article, name='article-update'),
    path('article/<int:pk>', get_article, name='article-details'),
]
