from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Місто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Місто"
        verbose_name_plural = "Міста"
        ordering = ['name']


class Point(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Місто')
    address = models.CharField(max_length=200, db_index=True, verbose_name='Адреса')
    pid = models.PositiveIntegerField(unique=True, verbose_name='Номер аптеки')

    def __str__(self):
        return str(self.pid)

    class Meta:
        verbose_name = "Точка"
        verbose_name_plural = "Точки"
        ordering = ['pid']


class Medicine(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Назва')
    qua = models.PositiveIntegerField(verbose_name='Кількість')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Ціна')
    code = models.PositiveIntegerField(verbose_name='Код')
    manufacture = models.CharField(max_length=100, verbose_name='Мануфактура')
    pid = models.CharField(max_length=10, verbose_name='Номер аптеки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Препарат"
        verbose_name_plural = "Препарати"
