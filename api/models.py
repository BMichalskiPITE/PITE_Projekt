from django.db import models
from rest_framework.reverse import reverse
# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200, default="none", null=True)
    photoRef = models.CharField(max_length=500,default="none")
    placeId = models.CharField(max_length=200,primary_key=True,default="none")
    vicinty = models.CharField(max_length=500,default="none")
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return str(self.name)

    def get_api_url(self, request = None):
        return reverse("places-rud", kwargs ={'placeId': self.placeId}, request = request)


class User(models.Model):
    user_id = models.CharField(max_length=200,primary_key=True)
    is_guide = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id)

    def get_api_url(self, request = None):
        return reverse("users-rud", kwargs ={'user_id': self.user_id}, request = request)

class Trip(models.Model):
    userId = models.CharField(max_length=200,primary_key=True)
    tripName = models.CharField(max_length=200, default="None")
    tripDescription = models.CharField(max_length=500, default="None")
    places = models.ManyToManyField(Place)
    guides = models.ManyToManyField(User)

    def __str__(self):
        return str(self.tripName)
