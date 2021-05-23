from rest_framework import viewsets
from department_app.models.department_models import Department
from department_app.serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()