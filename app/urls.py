# urls.py

from django.urls import path
from . import views
from app.forms import UserLoginForm,UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('settings/', views.settings, name='settings'),
    
    path('login/', LoginView.as_view(template_name="registration/login.html", authentication_form=UserLoginForm), name='login'),
    path('register/', views.register, name='register'),
    path('accounts/profile/',views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
    path('success/', views.success, name='success'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_list, name='search_list'),# Add success page URL# Add logout URL
    # Other URLs
    
]