from turtle import title
from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    creation_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'