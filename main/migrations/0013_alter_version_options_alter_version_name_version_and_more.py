# Generated by Django 4.2.6 on 2023-11-12 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
        migrations.AlterField(
            model_name='version',
            name='name_version',
            field=models.CharField(blank=True, null=True, verbose_name='Название версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='продукт'),
        ),
    ]
