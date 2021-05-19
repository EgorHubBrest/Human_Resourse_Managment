"""Serializer"""
from department_app.models import employee_model, department_models
from rest_framework import generics, permissions
from rest_framework import serializers
from django.contrib.auth.models import User


class DepartmentSerializer(serializers.ModelSerializer):
    """Department"""
    class Meta:
        model = department_models.Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """EmployeeSerializer"""
    class Meta:
        model = employee_model.Employee
        fields = '__all__'

#pylint: disable=W0223




# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

# Change Password


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)