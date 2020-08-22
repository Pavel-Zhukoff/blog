from django.db import models
from .blog import BlogModel
from .tag import TagModel

class ArticleModel(models.Model):

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(max_length=500, verbose_name='Текст статьи', help_text='Не более 500 символов')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    updation_date = models.DateField(auto_now=True, verbose_name='Дата обновления')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, verbose_name='Блог')
    tags = models.ManyToManyField(TagModel, verbose_name='Теги')
    draft = models.BooleanField(default=True, verbose_name='Черновик')

    class Meta:
        db_table = 'article'

        ordering = ['creation_date', 'title']

        verbose_name = 'статью'
        verbose_name_plural = 'Статьи'