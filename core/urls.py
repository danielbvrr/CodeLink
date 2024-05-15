from django.contrib import admin
from django.urls import path
from .views import post_list

urlpatterns = [
    path('posts/', post_list, name='index.html'),
]
