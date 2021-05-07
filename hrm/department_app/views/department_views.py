from rest_framework import viewsets
from department_app.models.department_models import Department
from department_app.serializers import DepartmentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


class DepartmentViewSet(viewsets.ViewSet):

    def list(self, request):
        departmnets = Department.objects.all()
        serializer = DepartmentSerializer(departmnets, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Department.objects.all()
        departmnet = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentSerializer(departmnet)
        return Response(serializer.data)

    def update(self, request, pk=None):
        departmnet = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(departmnet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        departmnet = Department.objects.get(pk=pk)
        departmnet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
