from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APITestCase
from department_app.models.employee_model import Employee
from department_app.models.department_models import Department
from department_app.views.department_views import DepartmentViewSet
from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient
import json

class EmployeeTests(APITestCase):
    def test_post_employee(self):
        url = reverse('department_app:employees-list')
        data =     {
        "name": "Anna Paul",
        "date": "1992-12-21",
        "email": "Anna@gmail.com",
        "department": 2
    }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.get(pk=response.json()['id']).name, 'Anna Paul')
        self.assertEqual(Employee.objects.get(pk=response.json()['id']).email, 'Anna@gmail.com')

    def test_get_department(self):
        url = reverse('department_app:employees-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_department(self):
        dep_exe = Department.objects.get(name='Executive Office')
        empl = Employee.objects.create(name='Anna Paul', department=dep_exe, date='1992-12-21',email='Anna@gmail.com')
        valid_empl = {
            "name" : "name is changed",
            "email": "email is changed"
        }
        response = self.client.put(
            reverse('department_app:employees-list', kwargs={'pk': empl.pk}),
            data = json.dumps(valid_empl),
            content_type = 'application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_destroy_department(self):
        dep_exe = Department.objects.get(name='Executive Office')
        empl = Employee.objects.create(name='Anna Paul', department=dep_exe, date='1992-12-21',email='Anna@gmail.com')
        response = self.client.put(
            reverse('department_app:employees-list', kwargs={'pk': empl.pk}),format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_for_pk_department(self):
        """Update department"""
        data = '{ "name": "Anna Paul","date": "1992-12-21","email": "Anna@gmail.com","department": 2}'
        dep_exe = Department.objects.get(name='Executive Office')
        empl = Employee.objects.create(name='Anna Paul', department=dep_exe, date='1992-12-21',email='Anna@gmail.com')
        url='http://127.0.0.1:8000/viewset/employee/'+str(empl.pk)+'/'
        response = self.client.put(url,data=data,content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Employee.objects.get(pk=empl.pk).name, 'Anna Paul')
        self.assertEqual(Employee.objects.get(pk=empl.pk).email, 'Anna@gmail.com')

        """Delete department"""
        res_delete = self.client.delete(url)
        self.assertEqual(res_delete.status_code, status.HTTP_204_NO_CONTENT)


    
    
