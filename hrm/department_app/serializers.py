"""Serializer"""
# pylint: disable=E5142
from department_app.models import employee_model, department_models
from django.contrib.auth.models import User
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    """Department"""
    class Meta:
        """Meta"""
        model = department_models.Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """EmployeeSerializer"""
    class Meta:
        """Meta"""
        model = employee_model.Employee
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """User Serializer"""
    class Meta:
        """Meta"""
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    """Register Serializer"""
    class Meta:
        """Meta"""
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


# pylint: disable=W0223
class ChangePasswordSerializer(serializers.Serializer):
    """Change Password"""
    model = User
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
