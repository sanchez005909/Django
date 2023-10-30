from django.contrib import admin
from main.models import Category, Product

# admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'price', 'category_id')
    list_filter = ('category_id', )
    search_fields = ('name_product', 'description',)
