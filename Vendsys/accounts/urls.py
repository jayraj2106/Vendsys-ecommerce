from django.urls import path
from .views import register_view,profile_view
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('profile/', profile_view, name='profile'),
]