from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name='категория')
    description = models.TextField(verbose_name='описание')
    # created_at = models.DateTimeField(default=timezone.now, verbose_name='дата создания', blank=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.id}) {self.name_category}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов


class Product(models.Model):
    name_product = models.CharField(max_length=50, verbose_name='название', null=True)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='категория', null=True)
    price = models.IntegerField(verbose_name='Цена', null=True)
    datetime_create = models.DateTimeField(default=timezone.now, verbose_name='дата создания', blank=True)
    datetime_changes = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения",
                                            blank=True)


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.id} {self.name_product} - {self.category}'

    class Meta:

        verbose_name = 'продукт' # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты' # Настройка для наименования набора объектов


