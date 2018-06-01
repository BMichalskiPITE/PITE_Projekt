from django.db import models
from rest_framework.reverse import reverse
# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    username = models.CharField(max_length =200, default = "None")
    mail = models.CharField(max_length = 200, default = "None")
    imageUrl = models.CharField(max_length = 500, default = "None")
    is_guide = models.BooleanField(default=False)
    gradesNumber = models.IntegerField(default = 0)
    gradesSum = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.username) 

    def get_api_url(self, request = None):
        return reverse("users-rud", kwargs ={'id': self.id}, request = request)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    fromUserId = models.CharField(max_length=200)
    toUserId = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)