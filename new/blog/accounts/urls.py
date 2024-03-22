"""define URL patterns for users"""
from django.contrib.auth import login

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # registration page
    path('register/', views.register, name='register'),
    # login page, include default auth urls
    path('login', views.login_request, name="login"),
    # log out
    path("logout", views.logout_request, name= "logout"),
]