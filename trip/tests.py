from rest_framework import status
from rest_framework.test import APIRequestFactory,APIClient,APITestCase
from django.contrib.auth import get_user_model
from place.models import Place
from user.models import User as User_model
from .models import Trip
from rest_framework.reverse import reverse
from .views import TripView
from .apps import TripConfig
from django.apps import apps

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

        user_m = User_model.objects.create(
            id = '24f',
            is_guide = True
            )
        user_tourist = User_model.objects.create(
            id = '13',
            is_guide = False
            )

        trip = Trip.objects.create(
            userId = '13',
            tripName = 'random name',
            tripDescription = 'decsription',
            )
        trip.places.add(place)

        trip2 = Trip.objects.create(
            userId = '13',
            tripName = 'another random trip',
            tripDescription = 'decsription',
            )
        trip2.places.add(place)
        trip2.guides.add(user_m)
    def test_str_method(self):
        trip = Trip.objects.get(pk = 1) 
        self.assertEqual(str(trip), trip.tripName)

    def test_add_item_trip(self):
        data = {
            'userId' : '13',
            'tripName' : 'kazimierz',
            'tripDescription' : 'wycieczka',
            'places' : [
                'ChIJjUf7MRBbFkcRg9Ls9752tqU'
            ]
        }
        url = reverse("trips-list")
        response = self.client.post(url, data, format='json')
        self.assertJSONEqual(str(response.content,encoding='utf8'),{'tripId': 3})
        self.assertEqual(response.status_code,200)

    def test_get_all_items_per_user_trip(self):
        response = self.client.get('/api/trips/?userid=13')

    def test_get_announce_list(self):
        data = {}
        url = reverse('trip-orders')
        response = self.client.get(url,data,format='json')
        self.assertEqual(response.status_code,200)

    def test_post_announce(self):
        data = {
            'userId' : '24f',
            'tripId' : 1,
        }
        url = reverse('trip-orders')
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,200)

    def test_delete_announce(self):
        data = {
            'userId' : '24f',
            'tripId' : 1,
        }
        url = reverse('trip-orders')
        self.client.post(url,data,format='json')
        response = self.client.delete(url,data,format='json')
        self.assertEqual(response.status_code,200)
        response = self.client.delete(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'this giude is not ordered to the trip'})

    def test_delete_announce_wrong_userid(self):
        data = {
            'userId' : '13',
            'tripId' : 1,
        }
        url = reverse('trip-orders')
        response = self.client.delete(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'this giude is not ordered to the trip'})
        
    def test_delete_announce_wrong_userid_2(self):
        data = {
            'userId' : '14f53',
            'tripId' : 1,
        }
        url = reverse('trip-orders')
        response = self.client.delete(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'no giudes with this ID'})
        
    def test_delete_announce_wrong_tripid(self):
        data = {
            'userId' : '13',
            'tripId' : 123,
        }
        url = reverse('trip-orders')
        response = self.client.delete(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'no trips with this ID'})
 
    def test_post_accept(self):
        data = {
            'userId' : '13',
            'tripId' : 2,
            'guideId' : '24f',
        }
        url = reverse('trip-acceptations')
        response = self.client.post(url,data,format = 'json')
        self.assertEqual(response.status_code,200)

    def test_post_accept_wrong_tripid(self):
        data = {
            'userId' : '13',
            'tripId' : 4824,
            'guideId' : '24f',
        }
        url = reverse('trip-acceptations')
        response = self.client.post(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'no trips with this ID'})


    def test_post_accept_wrong_tripid_or_userid(self):
        data = {
            'userId' : '24f',
            'tripId' : 2,
            'guideId' : '24f',
        }
        url = reverse('trip-acceptations')
        response = self.client.post(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'this trip does not belong to the user'})

    def test_post_accept_wrong_guideid(self):
        data = {
            'userId' : '13',
            'tripId' : 2,
            'guideId' : '15',
        }
        url = reverse('trip-acceptations')
        response = self.client.post(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'this giude is not ordered to the trip'})

    def test_post_accept_wrong_formula(self):
        data = {
            'userId' : '13',
            'tripId' : 2,
            'someradno' : 3832,
        }
        url = reverse('trip-acceptations')
        response = self.client.post(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'bad formula'})

    def test_delete_accept(self):
        data = {
            'userId' : '13',
            'tripId' : 2,
            'guideId' : '24f',
        }
        url = reverse('trip-acceptations')
        self.client.post(url,data,format = 'json')
        data = {
            'userId' : '13',
            'tripId' : 2,
            'guideId' : '24f',
        }
        response = self.client.delete(url,data,format = 'json')
        self.assertEqual(response.status_code,200)

    def test_delete_accept_wrong_tripid(self):
        data = {
            'userId' : '13',
            'tripId' : 2,
            'guideId' : '24f',
        }
        url = reverse('trip-acceptations')
        self.client.post(url,data,format = 'json')
        data = {
            'userId' : '13',
            'tripId' : 234,
            'guideId' : '24f',
        }
        response = self.client.delete(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'no trips with this ID'})

    def test_delete_accept_wrong_userid(self):
        data = {
            'userId' : '13',
            'tripId' : 2,
            'guideId' : '24f',
        }
        url = reverse('trip-acceptations')
        self.client.post(url,data,format = 'json')
        data = {
            'userId' : '14',
            'tripId' : 2,
            'guideId' : '24f',
        }
        response = self.client.delete(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'this trip does not belong to the user'})

    def test_delete_accept_wrong_guideid(self):
        data = {
            'userId' : '13',
            'tripId' : 2,
            'guideId' : '24f',
        }
        url = reverse('trip-acceptations')
        self.client.post(url,data,format = 'json')
        data = {
            'userId' : '13',
            'tripId' : 2,
            'guideId' : '22',
        }
        response = self.client.delete(url,data,format = 'json')
        self.assertEqual(response.status_code,422)
        self.assertJSONEqual(str(response.content, encoding= 'utf8'), {'form': 'this giude is not declared to the trip'})

    def test_apps(self):
        self.assertEqual(TripConfig.name,'trip')
        self.assertEqual(apps.get_app_config('trip').name, 'trip')
