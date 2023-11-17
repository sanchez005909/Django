from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from pytils.translit import slugify

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name='категория')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'Категория: {self.name_category}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='название', null=True)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    # slug = models.SlugField(null=False, unique=True, blank=True)
    image = models.ImageField(default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', null=True)
    price = models.IntegerField(verbose_name='Цена', null=True)
    datetime_create = models.DateTimeField(default=timezone.now, verbose_name='дата создания', blank=True)
    datetime_changes = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения",
                                            blank=True)
    user_prod = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='Пользователь')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.id}) {self.title} - {self.category}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов


class Version(models.Model):
    num_version = models.IntegerField(verbose_name='Номер версии')
    name_version = models.CharField(verbose_name='Название версии', **NULLABLE)
    is_active_version = models.BooleanField(default=False, verbose_name='Активность')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт', **NULLABLE)

    def __str__(self):
        return f'{self.name_version}'

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
