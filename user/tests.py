from rest_framework import status
from rest_framework.test import APIRequestFactory,APIClient,APITestCase
from django.contrib.auth import get_user_model
from .models import User as User_model
from rest_framework.reverse import reverse
from .apps import UserConfig
from django.apps import apps
from .serializers import UserSerializer

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
        user_test = User.objects.get(pk=1)
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

    def test_post_rudview_user_correct(self):
        user = User_model.objects.first()
        data = {
            'mail' : 'None',
            'id'   : '13',
            'username' : 'None',
            'imageUrl' : 'None',
            'is_guide' : 'True',
            'gradesNumber' : 1,
            'gradesSum' : 5,
        }
        url = user.get_api_url()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,200)

    def test_post_rudview_user_bad_id(self):
        user = User_model.objects.first()
        data = {
            'mail' : 'None',
            'id'   : '15',
            'username' : 'None',
            'imageUrl' : 'None',
            'is_guide' : 'False',
            'gradesNumber' : 1,
            'gradesSum' : 5,
        }
        url = user.get_api_url()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'no users with this ID'})

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

    def test_get_list_message(self):
        data = {}
        url = reverse("messages-list")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/messages/?id=13')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/messages/?userId=13')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_apps(self):
        self.assertEqual(UserConfig.name,'user')
        self.assertEqual(apps.get_app_config('user').name, 'user')

    def test_wrong_validation(self):
        data = {
            'id' : '24f',
            'username' : 'user2',
            'is_guide' : False
        }
        serializer = UserSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(set(serializer.errors.keys()), set(['id']))

    def test_correct_validation(self):
        data = {
            'id' : '34ic3rmi',
            'username' : 'user2',
            'is_guide' : False
        }
        serializer = UserSerializer(data=data)
        self.assertEqual(serializer.is_valid(), True)