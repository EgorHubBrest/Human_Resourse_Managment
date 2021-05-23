from django.urls import reverse
from rest_framework import status
from django.test import Client
from rest_framework.test import APITestCase
from department_app.models.employee_model import Employee
from department_app.models.department_models import Department
import json


class EmployeeTests(APITestCase):
    def test_post_employee(self):
        url = reverse('department_app:employees-list')
        data = {
            "name": "Anna Paul",
            "date": "1992-12-21",
            "email": "Anna@gmail.com",
            "department": 2
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.get(
            pk=response.json()['id']).name, 'Anna Paul')
        self.assertEqual(Employee.objects.get(
            pk=response.json()['id']).email, 'Anna@gmail.com')

    def test_post_employee_negative(self):
        url = reverse('department_app:employees-list')
        data = {
            "name": "",
            "date": "19692-162-261",
            "email": "",
            "department": 1000
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_employee(self):
        url = reverse('department_app:employees-list')
        response = self.client.get(url, format='json')
        true_data = {'id': 1,
                     'name': 'Maria Nankov',
                     'date': '1986-11-01',
                     'salary_currency': 'USD',
                     'salary': '1500.00',
                     'email': 'maria@gmail.com',
                     'status': 'Active',
                     'department': 1}
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_content[0], true_data)

    def test_put_employee(self):
        """Update department"""
        data = '{ "name": "Anna Paul","date": "1992-12-21","email": "Anna@gmail.com","department": 2}'
        dep_exe = Department.objects.get(name='Executive Office')
        empl = Employee.objects.create(
            name='Anna Paul', department=dep_exe, date='1992-12-21', email='Anna@gmail.com')
        url = reverse('department_app:employees-detail',
                      args=(empl.id,))
        response = self.client.put(
            url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Employee.objects.get(pk=empl.pk).name, 'Anna Paul')
        self.assertEqual(Employee.objects.get(
            pk=empl.pk).email, 'Anna@gmail.com')

    def test_put_employee_negative(self):
        """Update department"""
        data = '{ "name": "","date": "199422-124-2142","email": ","department": 1000}'
        dep_exe = Department.objects.get(name='Executive Office')
        empl = Employee.objects.create(
            name='Anna Paul', department=dep_exe, date='1992-12-21', email='Anna@gmail.com')
        url = reverse('department_app:employees-detail',
                      args=(empl.id,))
        response = self.client.put(
            url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destroy_employee(self):
        """Delete department"""
        dep_exe = Department.objects.get(name='Executive Office')
        empl = Employee.objects.create(
            name='Anna Paul', department=dep_exe, date='1992-12-21', email='Anna@gmail.com')
        url = reverse('department_app:employees-detail',
                      args=(empl.id,))
        res_delete = self.client.delete(url)
        self.assertEqual(res_delete.status_code, status.HTTP_204_NO_CONTENT)
