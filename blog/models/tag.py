from django.db import models

class TagModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'

        ordering = ['name']

        verbose_name = 'тег'
        verbose_name_plural = 'Теги'