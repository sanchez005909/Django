# Generated by Django 4.2.6 on 2023-11-08 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_product_name_product_product_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]