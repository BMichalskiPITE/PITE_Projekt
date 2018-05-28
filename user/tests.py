from rest_framework import status
from rest_framework.test import APIRequestFactory,APIClient,APITestCase
from django.contrib.auth import get_user_model
from .models import User as User_model
from rest_framework.reverse import reverse
from .apps import UserConfig
from django.apps import apps

User = get_user_model()

class PlaceTestCase(APITestCase):
    def setUp(self):
        user = User(username='testcfuser', email='test@test.com')
        user.set_password("qwerty")
        user.save()

        user_m = User_model.objects.create(
            id = '24f',
            username = 'user1',
            is_guide = True
            )
        user_tourist = User_model.objects.create(
            id = '13',
            is_guide = False
            )

    def test_str_method(self):
        user_test = User.objects.get(pk = 1)
        self.assertEqual(str(user_test), user_test.username)

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
        data = {'id':'344034sf', 'is_guide':True}
        url = user.get_api_url()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item_user(self):
        data = {"id" : "4230", "is_guide": False}
        url = reverse("users-list")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_apps(self):
        self.assertEqual(UserConfig.name,'user')
        self.assertEqual(apps.get_app_config('user').name, 'user')
