from rest_framework import generics, mixins
from .models import Place
from .serializers import PlaceSerializer
from django.db.models import Q
from .forms import PlaceForm
from django.http import JsonResponse

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

