from django.http import response
from django.urls import reverse
from rest_framework import status
from django.test import Client
from rest_framework.test import APITestCase
import json


class UserTests(APITestCase):
    def test_user(self):
        url = reverse('department_app:register')
        data = {
            "username": "use42341r5",
            "email": "u41523ser342@user.user",
            "password": "qwrw75765reasdzxc"
        }
        response_reg = self.client.post(url, data, format='json')
        self.assertEqual(response_reg.status_code, status.HTTP_200_OK)
        url = reverse('department_app:login')
        data = {
            "username": "use42341r5",
            "password": "qwrw75765reasdzxc"
        }
        response_login = self.client.post(url, data, format='json')
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)
        response_content = json.loads(response_login.content.decode('utf-8'))
        url = reverse('department_app:user')
        response_user = self.client.get(
            url, HTTP_AUTHORIZATION='Token {}'.format(response_content['token']))
        self.assertEqual(response_user.status_code, status.HTTP_200_OK)

        url = reverse('department_app:change-password')
        data = {
            "old_password": "qwrw75765reasdzxc",
            "new_password": "Newqwrw75765reasdzxc"
        }
        response_user_put = self.client.put(
            url, data, HTTP_AUTHORIZATION='Token {}'.format(response_content['token']))
        self.assertEqual(response_user_put.status_code, status.HTTP_200_OK)
