from rest_framework import generics, mixins
from .models import User
from trip.models import Trip
from .serializers import UserSerializer
from trip.serializers import TripSerializer
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers


class UserView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'id'
    serializer_class    = UserSerializer
    
    def get_queryset(self):
        qs = User.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(id__icontains=query))
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        = 'id'
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}