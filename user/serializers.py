from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = [
        'url',
        'id',
        'username',
        'mail',
        'imageUrl',
        'gradesNumber',
        'gradesSum'
        ]

    def get_url(self,obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_name(self,value):
        qs = User.objects.filter(id__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This user already exists")
