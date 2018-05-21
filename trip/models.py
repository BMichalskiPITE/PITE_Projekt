from django.db import models
from rest_framework.reverse import reverse
from place.models import Place
from user.models import User
# Create your models here.

class Trip(models.Model):
    userId = models.CharField(max_length=200,primary_key=True)
    tripName = models.CharField(max_length=200, default="None")
    tripDescription = models.CharField(max_length=500, default="None")
    places = models.ManyToManyField(Place)
    guides = models.ManyToManyField(User)

    def __str__(self):
        return str(self.tripName)
