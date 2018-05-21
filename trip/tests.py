from rest_framework import status
from rest_framework.test import APIRequestFactory,APIClient,APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

User = get_user_model()

class TripTestCase(APITestCase):
    def setUp(self):
        user = User(username='testcfuser', email='test@test.com')
        user.set_password("qwerty")
        user.save()

