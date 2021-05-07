from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APITestCase
from department_app.models.department_models import Department
from department_app.views.department_views import DepartmentViewSet
from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient
import json

class DepartmentTests(APITestCase):
    def test_post_department(self):
        url = reverse('department_app:departments-list')
        data = {'name': 'Develope','status':'Active'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.get(pk=response.json()['id']).name, 'Develope')
        self.assertEqual(Department.objects.get(pk=response.json()['id']).status, 'Active')

    def test_get_department(self):
        url = reverse('department_app:departments-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_department(self):
        dev = Department.objects.create(name="Dev1", status="Active")
        valid_dev = {
            "name" : "name is changed",
            "status": "status is changed"
        }
        response = self.client.put(
            reverse('department_app:departments-list', kwargs={'pk': dev.pk}),
            data = json.dumps(valid_dev),
            content_type = 'application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_destroy_department(self):
        dev = Department.objects.create(name="Dev1", status="Active")
        response = self.client.put(
            reverse('department_app:departments-list', kwargs={'pk': dev.pk}),format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_for_pk_department(self):
        """Update department"""
        data = '{"name": "Egor","status":"Active"}'
        department = Department.objects.create(name='Dev1',status='Inactive')

        url = reverse('department_app:departments-detail', args=(department.id,))
        response = self.client.put(url,data=data,content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Department.objects.get(pk=department.pk).name, 'Egor')
        self.assertEqual(Department.objects.get(pk=department.pk).status, 'Active')

        """Delete department"""
        res_delete = self.client.delete(url)
        self.assertEqual(res_delete.status_code, status.HTTP_204_NO_CONTENT)


    
    
