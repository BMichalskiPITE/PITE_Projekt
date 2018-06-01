from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Trip
        fields = [
        'url',
        'pk',
        'userId',
        'tripName',
        'tripDescription',
        'places',
        'guides',
        'declaredGuide',
        'isDeclared'
        ]


    def get_url(self,obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_name(self,value):
        qs = Trip.objects.filter(tripName__iexact=value).filter(userId__iexact=value)
        if self.instance:
            qs = qs.exclude(pk = self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This trip already exists")