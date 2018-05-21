from rest_framework import serializers
from trip.models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
        'pk',
        'userId',
        'tripName',
        'tripDescription',
        'places',
        'guides'
        ]

        read_only_fields = ['userId']

    def validate_name(self,value):
        qs = Trip.objects.filter(tripName__iexact=value).filter(userId__iexact=value)
        if self.instance:
            qs = qs.exclude(pk = self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This trip already exists")