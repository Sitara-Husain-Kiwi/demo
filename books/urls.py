from django import views
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.Index.as_view(), name='index'),
    path('home', views.home, name='home'),
    # path('edit', views.edit, name='edit'),
    # path('delete', views.delete, name='delete'),
]