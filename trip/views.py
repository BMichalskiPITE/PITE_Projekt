from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from .models import Trip
from user.models import User
from .forms import TripForm, AnnounceTripForm, AcceptTripForm
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
    lookup_field = 'pk'
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


@api_view(['GET','POST','DELETE'])
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
                return JsonResponse({'form': 'no trips with this ID'}, status=422)
            guide = guide.filter(Q(id__icontains=form.clean_userId()))
            if guide.count() > 0:
                guide = guide[0]
            else:
                return JsonResponse({'form': 'no guides with this ID'}, status=422)
            if guide.is_guide is False:
                return JsonResponse({'form': 'this user is not a guide'}, status=422)
            trip.save()
            trip.guides.add(guide)
            trip.save()
            serializer = TripSerializer(trip)
            return JsonResponse(serializer.data, safe = False)

    if request.method == 'GET':
        trips = Trip.objects.filter(declaredGuide = "None")
        serializer = TripSerializer(trips, many = True)
        return JsonResponse(serializer.data, safe = False)

    if request.method == 'DELETE':
        trip = Trip.objects.all()
        guide = User.objects.all()
        form = AnnounceTripForm(request.data)
        if form.is_valid():
            trip = trip.filter(Q(id__icontains=form.clean_tripId()))
            if trip.count() > 0:
                trip = trip[0]
            else:
                return JsonResponse({'form': 'no trips with this ID'}, status=422)
            guide = guide.filter(Q(id__icontains=form.clean_userId()))
            if guide.count() > 0:
                guide = guide[0]
            else:
                return JsonResponse({'form': 'no giudes with this ID'}, status=422)
            if trip.guides.filter(Q(id__icontains = form.clean_userId())).count() == 0:
                return JsonResponse({'form': 'this giude is not ordered to the trip'}, status=422)
            trip.guides.remove(guide)
            trip.save()
            serializer = TripSerializer(trip)
            return JsonResponse(serializer.data, safe=True)

@api_view(['POST','DELETE'])
def trip_acceptation_list(request, format = None):

    if request.method == 'POST':
        form = AcceptTripForm(request.data)
        if form.is_valid():
            trip = Trip.objects.filter(Q(id__icontains=form.clean_tripId()))
            if trip.count() == 1:
                trip = trip[0]
            else: return JsonResponse({'form' : 'no trips with this ID'}, status = 422)    
            if trip.userId != form.clean_userId() : return JsonResponse({'form' : 'this trip does not belong to the user'}, status=422)
            if trip.guides.filter(Q(id__icontains = form.clean_guideId())).count() == 0:
                return JsonResponse({'form': 'this giude is not ordered to the trip'}, status=422)
            trip.isDeclared = True
            trip.declaredGuide = form.clean_guideId()
            trip.save()
            serializer = TripSerializer(trip)
            return JsonResponse(serializer.data, safe=True)
        else: return JsonResponse({'form' : 'bad formula'}, status=422)

    if request.method == 'DELETE':
        form = AcceptTripForm(request.data) 
        if form.is_valid():
            trip = Trip.objects.filter(Q(id__icontains=form.clean_tripId()))
            if trip.count() == 1:
                trip = trip[0]
            else: 
                return JsonResponse({'form' : 'no trips with this ID'}, status = 422)    
            if trip.userId != form.clean_userId() : 
                return JsonResponse({'form' : 'this trip does not belong to the user'}, status=422)
            if trip.declaredGuide != form.clean_guideId():
                return JsonResponse({'form': 'this giude is not declared to the trip'}, status=422)
            guide = User.objects.filter(Q(id__icontains=form.clean_guideId()))
            guide = guide[0]
            trip.isDeclared = False
            trip.declaredGuide = "None"
            trip.guides.remove(guide)
            trip.save()
            serializer = TripSerializer(trip)
            return JsonResponse(serializer.data, safe=True)
        else: 
            return JsonResponse({'form' : 'bad formula'}, status=422)


