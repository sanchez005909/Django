from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import MaterialCreateView, MaterialListView, MaterialDetailView, MaterialUpdateView, \
    MaterialDeleteView

app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', MaterialCreateView.as_view(), name='create'),
    path('', MaterialListView.as_view(), name='material'),
    path('view/<int:pk>/', MaterialDetailView.as_view(), name='material_detail'),
    path('update/<int:pk>/', MaterialUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)