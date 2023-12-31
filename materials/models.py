from django.db import models


class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название статьи')
    slug = models.CharField(max_length=150, verbose_name='slug')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(null=True, blank=True)
    datetime_create = models.DateField(auto_now=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
