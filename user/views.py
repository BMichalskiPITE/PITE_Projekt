from rest_framework import generics, mixins, filters
from .models import User,Message
from trip.models import Trip
from .serializers import UserSerializer,MessageSerializer
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

class MessagesView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        userId = self.request.query_params.get('userId', None)

        if id is not None:
            return Message.objects.filter(id=id)    
        
        if userId is not None:
            return Message.objects.filter(Q(fromUserId=userId) | Q(toUserId=userId))

        return Message.objects.all()

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)