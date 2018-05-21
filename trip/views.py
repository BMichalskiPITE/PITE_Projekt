from rest_framework import generics, mixins
from trip.models import Trip
from trip.serializers import TripSerializer
from django.db.models import Q

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

class TripRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.all()