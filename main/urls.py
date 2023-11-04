from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from main.apps import MainConfig
from main.views import contact, ProductListView, ProductDetailView


app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contact', contact, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




