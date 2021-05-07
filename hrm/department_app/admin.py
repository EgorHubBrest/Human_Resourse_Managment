from django.contrib import admin

from department_app.models import employee_model, department_models,users_models

admin.site.register(employee_model.Employee)
admin.site.register(department_models.Department)
admin.site.register(users_models.User)
