from django.urls import path
from main.views import index, contact
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', index),
    path('contact', contact, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



