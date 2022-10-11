from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.login_view, name='login_page'),
    path('register/', views.register_view, name='register_page'),
    path('logout/', views.logout_view, name='logout_page')
]