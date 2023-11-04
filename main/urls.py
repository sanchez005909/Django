from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from main.apps import MainConfig
from main.views import (contact, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                        ProductDeleteView)

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contact', contact, name='contact'),
    path('product_create', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]



