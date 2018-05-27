from django.db import models
from rest_framework.reverse import reverse
# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    username = models.CharField(max_length =200, default = "None")
    mail = models.CharField(max_length = 200, default = "None")
    imageUrl = models.CharField(max_length = 500, default = "None")
    is_guide = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_api_url(self, request = None):
        return reverse("users-rud", kwargs ={'id': self.id}, request = request)
