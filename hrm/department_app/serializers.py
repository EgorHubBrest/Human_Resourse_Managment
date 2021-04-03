"""Serializer"""
from rest_framework import serializers

from department_app.models.department_models import Department

from department_app.models.employee_model import Employee


class DepartmentSerializer(serializers.ModelSerializer):
    """DepartmentTable"""
    class Meta:
        """MetaClass"""
        model = Department
        fields = ['name', 'status']


class EmployeeSerializer(serializers.ModelSerializer):
    """EmployeeTable"""
    class Meta:
        """MetaClass"""
        model = Employee
        fields = ['id', 'name', 'department',
                  'date', 'salary', 'email', 'status']
