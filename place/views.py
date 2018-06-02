from rest_framework import generics, mixins
from rest_framework import viewsets
from .models import Place
from .serializers import PlaceSerializer
from django.db.models import Q
from .forms import PlaceForm
from django.http import JsonResponse
import urllib.request, json 
import time

class PlaceView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'placeId'
    serializer_class    = PlaceSerializer

    def get_queryset(self):
        qs = Place.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(name__icontains=query)|Q(vicinty__icontains=query)).distinct()
        return qs

    def post(self,request,*args,**kwargs):
        form = PlaceForm(request.data)
        if form.is_valid():
            place = form.save()
            place.name = form.clean_name()
            place.save()
            serializer = PlaceSerializer(place)
            return JsonResponse(serializer.data, safe = False)
        return JsonResponse({'place':'not allowed formula'}, status=422)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class PlaceRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        = 'placeId'
    serializer_class    = PlaceSerializer

    def get_queryset(self):
        return Place.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class PlaceSyncView(viewsets.ViewSet):

    def sync(self, request):
        debug = []
        gmaps_api_key = "AIzaSyDXJPkrTmAaD6AhH_7vFHBYxOEB1KZdqWo"
        gmaps_location = "50.062533,19.93732"
        gmaps_radius = "15000"
        gmaps_type = "museum"
        gmaps_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0}&radius={1}&type={2}&key={3}".format(gmaps_location,gmaps_radius,gmaps_type,gmaps_api_key)
        gmaps_next_page_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={0}&pagetoken=".format(gmaps_api_key)
        max_pages = 5
        interval_sec = 3

        debug.append(gmaps_url)

        places_loaded = 0
        page = -1
        gmaps_next_url = gmaps_url
        next_token = ""
        while True:
            debug.append(gmaps_next_url)
            with urllib.request.urlopen(gmaps_next_url) as url:
                response = json.loads(url.read().decode())
                next_token = response["next_page_token"] if "next_page_token" in response else None
                places = self.get_places(response)
                self.save_places(places)
                places_loaded += len(places)
                time.sleep(interval_sec) 
            if next_token is None or page >= max_pages:
                break
            gmaps_next_url = gmaps_next_page_url + next_token
            page = page + 1

        data = {}
        data['debug'] = debug
        data['places_loaded'] = places_loaded
        return JsonResponse(data, status=200)

    def get_places(self, response):
        places = []
        for place in response["results"]:
            try:
                places.append({
                    'placeId': place["place_id"],
                    'name': place["name"],
                    'photoRef': place["photos"][0]["photo_reference"],
                    'vicinity': place["vicinity"],
                    'latitude': place["geometry"]["location"]["lat"],
                    'longitude': place["geometry"]["location"]["lng"],
                })
            except Exception as e:
                print("Exception during synchronization: " + str(e))

        return places

    def save_places(self, places):
        for place in places:
            newPlace = Place(placeId=place["placeId"],name=place["name"],photoRef=place["photoRef"],vicinty=place["vicinity"],latitude=float(place["latitude"]),longitude=float(place["longitude"]))
            newPlace.save()

