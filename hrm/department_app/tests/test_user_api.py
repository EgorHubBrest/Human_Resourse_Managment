from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APITestCase
from department_app.models.users_models import User
from department_app.models.employee_model import Employee
from department_app.models.department_models import Department
from department_app.views.department_views import DepartmentViewSet
from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient
import json

class UserTests(APITestCase):
    def test_user(self):
        url = reverse('department_app:user-reg')
        data = {
        'user':{
        "username": "use42341r5",
        "email": "u41523ser342@user.user",
        "password": "qwrw75765reasdzxc"
        }
        }
        response_reg = self.client.post(url, data, format='json')
        self.assertEqual(response_reg.status_code, status.HTTP_201_CREATED)

        response_content_reg = json.loads(response_reg.content.decode('utf-8'))
        token = response_content_reg['user']['token']

        url = reverse('department_app:user-login')
        data = {
        'user':{
        "email": "u41523ser342@user.user",
        "password": "qwrw75765reasdzxc"
        }
        }
        response_login = self.client.post(url, data, format='json')
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)
        url =reverse('department_app:user')
        response_user = self.client.get(url,HTTP_AUTHORIZATION='Token {}'.format(token))
        self.assertEqual(response_user.status_code, status.HTTP_200_OK)
        data ={
                  'user':{
        "email": "Egotu41523ser342@user.user"
        }
        }
        response_user_patch = self.client.patch(url,data,HTTP_AUTHORIZATION='Token {}'.format(token))
        response_content_patch = json.loads(response_user_patch.content.decode('utf-8'))['user']['email']
        self.assertEqual(response_user_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(response_content_patch, "Egotu41523ser342@user.user")

        