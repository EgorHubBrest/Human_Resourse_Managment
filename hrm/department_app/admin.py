"""Django Admin"""
from django.contrib import admin 

from department_app.models import department,employees

admin.site.register(department.Department)
admin.site.register(employees.Employees)