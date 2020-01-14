from django.db import models

# Create your models here.

class Zakupki(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    cost = models.CharField(max_length=25, verbose_name="Цена")
    link = models.CharField(max_length=255, verbose_name="Ссылка")
    class Meta:
        verbose_name="Парсинг проектов"
        verbose_name_plural="Парсинг проектов"
