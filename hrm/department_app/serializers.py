from rest_framework import serializers

from department_app.models.department_models import Department

from department_app.models.employee_model import Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'status']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department',
                  'date', 'salary', 'email', 'status']
