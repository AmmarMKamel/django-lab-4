from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='myauth.home'),
    path('register', views.register, name='myauth.register'),
    path('login', views.login, name='myauth.login'),
    path('logout', views.logout, name='myauth.logout'),
]