from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from users.apps import UsersConfig
from users.views import RegisterView, EmailVerify, ProfileView, generate_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('Logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(template_name='users/user_form.html'), name='profile'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
