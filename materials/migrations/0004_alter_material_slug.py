# Generated by Django 4.2.6 on 2023-11-01 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_remove_material_data_create_material_datetime_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=models.SlugField(max_length=150, verbose_name='slug'),
        ),
    ]
