from django.contrib import admin

from department_app.models import employee_model, department_models
admin.site.register(employee_model.Employee)
admin.site.register(department_models.Department)
