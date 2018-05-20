from rest_framework import serializers
from api.models import Place,User,Trip

class PlaceSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Place
        fields = [
            'url',
            'name',
            'photoRef',
            'placeId',
            'vicinty',
            'latitude',
            'longitude'
            ]

    def get_url(self,obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_name(self,value):
        qs = Place.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(placeId = self.instance.placeId)
        if qs.exists():
            raise serializers.ValidationError("This place already exists")


class UserSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = [
        'url',
        'user_id',
        'is_guide'
        ]

    def get_url(self,obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_name(self,value):
        qs = User.objects.filter(user_id__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This user already exists")

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