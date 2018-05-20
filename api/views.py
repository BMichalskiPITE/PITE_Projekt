"""from django.contrib.auth.models import Group
from api.models import Place, User
from rest_framework import viewsets,status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.serializers import PlaceSerializer,UserSerializer

class PlaceView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    model = Place
    serializer_class = PlaceSerializer

class UserView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            user = User(user_id=user_id,is_guide=False)
            user.save()
            
        return Response(UserSerializer(user).data)

    def put(self, request, user_id):
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            user = User(user_id=user_id,is_guide=False)
            user.save()

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

from rest_framework import generics, mixins
from api.models import Place, User, Trip
from api.serializers import PlaceSerializer,UserSerializer, TripSerializer
from django.db.models import Q

class PlaceView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field        = 'placeId'
    serializer_class    = PlaceSerializer

    def get_queryset(self):
        qs = Place.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(name__icontains=query)|Q(vicinty__icontains=query)).distinct()
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field        = 'user_id'
    serializer_class    = UserSerializer
    
    def get_queryset(self):
        qs = User.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(user_id__icontains=query))
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class TripView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = TripSerializer

    def get_queryset(self):
        qs = Trip.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(tripName__icontains=query))
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

class PlaceRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field        = 'placeId'
    serializer_class    = PlaceSerializer

    def get_queryset(self):
        return Place.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class UserRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field        = 'user_id'
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class TripRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.all()