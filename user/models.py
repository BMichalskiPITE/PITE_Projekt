from django.db import models
from rest_framework.reverse import reverse
# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=200,primary_key=True)
    is_guide = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id)

    def get_api_url(self, request = None):
        return reverse("users-rud", kwargs ={'user_id': self.user_id}, request = request)
