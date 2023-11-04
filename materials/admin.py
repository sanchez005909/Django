from django.contrib import admin

from materials.models import Material


# Register your models here.

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'slug',
                    'image',
                    'is_published')
