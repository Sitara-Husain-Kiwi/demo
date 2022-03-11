from django import views
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.Index.as_view(), name='index'),
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
]