# Generated by Django 4.2.6 on 2023-10-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_product_name_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name_product',
            field=models.CharField(max_length=50, null=True, verbose_name='название'),
        ),
    ]
