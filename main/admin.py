from django.contrib import admin
from main.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category_id')
    list_filter = ('category_id', )
    search_fields = ('title', 'description',)
