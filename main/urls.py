from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from main.apps import MainConfig
from main.views import (contact, CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
                        ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
                        toggle_published)

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('category_list', CategoryListView.as_view(), name='category_list'),
    path('category_create', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contact', contact, name='contact'),
    path('product_create', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('published_product/<int:pk>/', toggle_published, name='is_published')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



