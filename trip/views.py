from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from .models import Trip
from user.models import User
from .forms import TripForm, AnnounceTripForm
from .serializers import TripSerializer
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers

class TripView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = TripSerializer

    def get_queryset(self):
        qs = Trip.objects.all()
        query = self.request.GET.get("userid")
        if query is not None:
            qs = qs.filter(Q(userId__icontains=query))
        query = self.request.GET.get("tripid")
        if query is not None:
            qs = qs.filter(Q(pk__icontains=query))
        return qs

    def post(self,request):
        if request.method == "POST":
            form = TripForm(request.data)
            if form.is_valid():
                trip = form.save()
                trip.save()
                return JsonResponse({'tripId' : trip.pk})
            else:
                 return JsonResponse({'trip': form.errors}, status=422)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class TripRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


@api_view(['GET','POST'])
def trip_announce_list(request, format = None):

    if request.method == 'POST':
        trip = Trip.objects.all()
        guide = User.objects.all()
        form = AnnounceTripForm(request.data)
        if form.is_valid():
            trip = trip.filter(Q(id__icontains=form.clean_tripId()))
            if trip.count() > 0:
                trip = trip[0]
            else:
                return JsonResponse({'form': form.errors}, status=422)
            guide = guide.filter(Q(id__icontains=form.clean_userId()))
            if guide.count() > 0:
                guide = guide[0]
            else:
                return JsonResponse({'form': form.errors}, status=422)
            if guide.is_guide is False:
                return JsonResponse({'form': form.errors}, status=422)
            trip.save()
            trip.guides.add(guide)
            serializer = TripSerializer(trip)
            return JsonResponse(serializer.data, safe = False)
    if request.method == 'GET':
        trips = Trip.objects.filter(guides=None)
        serializer = TripSerializer(trips, many = True)
        return JsonResponse(serializer.data, safe = False)