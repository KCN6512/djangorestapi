from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse

class Actor(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    content = models.TextField(blank=True,verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category',null=True,verbose_name='Категория',on_delete=models.SET_NULL)
    slug = AutoSlugField(populate_from='title',verbose_name='URL',unique=True,editable=True)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True,verbose_name='Категория')

    def __str__(self) -> str:
        return self.name
