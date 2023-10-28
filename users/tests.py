from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_user(self):
        url = reverse('users:create-user')
        data = {
            "username": "testuser",
            "password": "123"
        }

        response = self.client.post(url, data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
