from rest_framework import serializers
from .models import User,Message

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
        'is_guide',
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


class MessageSerializer(serializers.ModelSerializer):
     class Meta:
        model = Message
        fields = [
        'id',
        'fromUserId',
        'toUserId',
        'message',
        'date'
        ]
