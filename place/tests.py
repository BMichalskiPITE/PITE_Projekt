from rest_framework import status
from rest_framework.test import APIRequestFactory,APIClient,APITestCase
from django.contrib.auth import get_user_model
from .models import Place
from rest_framework.reverse import reverse
from .apps import PlaceConfig
from django.apps import apps
from .serializers import PlaceSerializer

User = get_user_model()

class PlaceTestCase(APITestCase):
    def setUp(self):
        user = User(username='testcfuser', email='test@test.com')
        user.set_password("qwerty")
        user.save()
        place = Place.objects.create(
            name='Kraków Barbican',
            photoRef='CmRaAAAA5BVnVf3jbhlpkmnjhzDF_lSr9y0fuMFqjDUe6j8a4AvyoCwPf1jKUp6wyeisieoQuPvArPQ7_GXXkX3j9a4HWowGHcDR-V5SvQ_R5iVj7h5RMwbpBzlw9_rC0FYdw6S0EhC9kT0XSOERfzAF9ONCtvhrGhRLaEz1k5gAK-ZLki8v9jkfjrt4hA',
            placeId= 'ChIJjUf7MRBbFkcRg9Ls9752tqU',
            vicinty= 'Basztowa, Kraków',
            latitude= 50.0654718,
            longitude=19.9416613
            )
        
    def test_str_method(self):
        place = Place.objects.get(placeId = 'ChIJjUf7MRBbFkcRg9Ls9752tqU')
        self.assertEqual(str(place), place.name) 

    def test_single_place(self):
        place_count = Place.objects.count()
        self.assertEqual(place_count, 1)

    def test_get_list_place(self):
        data = {}
        url = reverse("places-list")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item_place(self):
        place = Place.objects.first()
        data = {}
        url = place.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_update_place(self):
        place = Place.objects.first()
        data = {'name':'rand', "photoRef": "ffhsf", "placeId": "348794", "vicinty": "rynek glowny", "latitude": 20, "longitude": 50}
        url = place.get_api_url()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item_place(self):
        data = {'name': 'rando place', 'photoRef':'s3e3982', "placeId": "348794", 'vicinty': 'tesei 2', 'latitude':21, 'longitude':45}
        url = reverse("places-list")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_apps(self):
        self.assertEqual(PlaceConfig.name,'place')
        self.assertEqual(apps.get_app_config('place').name, 'place')

    def test_wrong_validation(self):
        data = {
            'name' : 'Kraków Barbican',
            'photoRef' : 'rwru0',
            'placeId' : 'er2rweu',
            'vicinty' : 'Basztowa, Kraków',
            'latitude' : 50.0654718,
            'longitude' : 19.9416613
        }
        serializer = PlaceSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(set(serializer.errors.keys()), set(['name']))

    def test_correct_validation(self):
        data = {
            'name' : 'Barbican',
            'photoRef' : 'rwru0',
            'placeId' : 'er2rweu',
            'vicinty' : 'Basztowa, Kraków',
            'latitude' : 50.0654718,
            'longitude' : 19.9416613
        }
        serializer = PlaceSerializer(data=data)
        self.assertEqual(serializer.is_valid(), True)

    def test_get_sync_places(self):
        data = {}
        response = self.client.get('/api/sync/places/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)