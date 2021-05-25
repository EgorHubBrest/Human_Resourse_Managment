from rest_framework import viewsets
from department_app.models.employee_model import Employee
from department_app.serializers import EmployeeSerializer


class EmployeetViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
