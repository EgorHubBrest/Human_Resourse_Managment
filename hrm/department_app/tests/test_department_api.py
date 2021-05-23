from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from department_app.models.department_models import Department
import json


class DepartmentTests(APITestCase):
    def test_post_department(self):
        url = reverse('department_app:departments-list')
        data = {'name': 'Develope', 'status': 'Active'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.get(
            pk=response.json()['id']).name, 'Develope')
        self.assertEqual(Department.objects.get(
            pk=response.json()['id']).status, 'Active')

    def test_post_department_negative(self):
        url = reverse('department_app:departments-list')
        data = {'name': '', 'status': 'Error'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_department(self):
        url = reverse('department_app:departments-list')
        response = self.client.get(url, format='json')
        true_data = {'id': 1, 'name': 'Executive Office', 'status': 'Active'}
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_content[0], true_data)

    def test_put_department(self):
        data = '{"name": "Egor","status":"Active"}'
        department = Department.objects.create(
            name='Dev1', status='Inactive')

        url = reverse('department_app:departments-detail',
                      args=(department.id,))
        response = self.client.put(
            url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Department.objects.get(pk=department.pk).name, 'Egor')
        self.assertEqual(Department.objects.get(
            pk=department.pk).status, 'Active')

    def test_put_department_negative(self):
        data = '{"name": "","status":"Wrong"}'
        department = Department.objects.create(
            name='Dev1', status='Inactive')

        url = reverse('department_app:departments-detail',
                      args=(department.id,))
        response = self.client.put(
            url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destroy_department(self):
        department = Department.objects.create(
            name='Dev1', status='Inactive')
        url = reverse('department_app:departments-detail',
                      args=(department.id,))
        res_delete = self.client.delete(url)
        self.assertEqual(res_delete.status_code, status.HTTP_204_NO_CONTENT)
