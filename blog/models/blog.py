from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        error_messages={'blank': 'Поле не может быть пустым', 'unique': 'Название должно быть уникальным'},
        verbose_name='Название блога'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор блога')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog'

        verbose_name = 'блог'
        verbose_name_plural = 'Блоги'