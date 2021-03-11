"""URLS"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',include('department_app.urls')),
    path('admin/', admin.site.urls),
]
