from django.contrib import admin
from .models.tag import TagModel
from .models.article import ArticleModel
from .models.blog import BlogModel

# Register your models here.
admin.site.register([TagModel, ArticleModel, BlogModel])