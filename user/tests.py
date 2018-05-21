from rest_framework import status
from rest_framework.test import APIRequestFactory,APIClient,APITestCase
from django.contrib.auth import get_user_model
from api.models import User as User_model
from rest_framework.reverse import reverse

User = get_user_model()

class UserTestCase(APITestCase):
    def setUp(self):
        user = User(username='testcfuser', email='test@test.com')
        user.set_password("qwerty")
        user.save()
        user_m = User_model.objects.create(
            user_id = '24f',
            is_guide = True
            )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_get_list_user(self):
        data = {}
        url = reverse("users-list")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item_user(self):
        user = User_model.objects.first()
        data = {}
        url = user.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_update_user(self):
        user = User_model.objects.first()
        data = {'user_id':'344034sf', 'is_guide':True}
        url = user.get_api_url()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item_user(self):
        data = {"user_id" : "4230", "is_guide": False}
        url = reverse("users-list")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


