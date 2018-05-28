from django.db import models
from rest_framework.reverse import reverse
from user.models import User
from place.models import Place

class Trip(models.Model):
    userId = models.CharField(max_length=200, default="None")
    tripName = models.CharField(max_length=200, default="None")
    tripDescription = models.CharField(max_length=500, default="None")
    places = models.ManyToManyField(Place)
    guides = models.ManyToManyField(User)
    declaredGuide = models.CharField(max_length = 200, default = "None")
    isDeclared = models.BooleanField(default = False)

    def __str__(self):
        return str(self.tripName)

    def get_api_url(self, request = None):
        return reverse("trips-rud", kwargs ={'pk': self.pk}, request = request)