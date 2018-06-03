from rest_framework import generics, mixins, filters
from .models import User,Message
from trip.models import Trip
from .serializers import UserSerializer,MessageSerializer
from trip.serializers import TripSerializer
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from .forms import UserForm, AnnounceUserForm
from pprint import pprint

 


class UserView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'id'
    serializer_class    = UserSerializer
    
    def get_queryset(self):
        qs = User.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(id__icontains=query))
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        = 'id'
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user = User.objects.all()
            form = AnnounceUserForm(request.data)
            if form.is_valid():
                user = user.filter(Q(id__icontains=form.clean_id()))
                if user.count() > 0:
                    user = user[0]
                else:
                    return JsonResponse({'form': 'no users with this ID'}, status=422)
        
                user.mail = form.clean_mail()

                user.id = form.clean_id()
                
                user.username = form.clean_username()

                user.imageUrl = form.clean_imageUrl()
                user.is_guide = form.clean_is_guide()

                if (form.clean_gradesNumber() == None):
                    user.gradesNumber = 0
                else:
                    user.gradesNumber = form.clean_gradesNumber()

                if (form.clean_gradesSum() == None):
                    user.gradesSum = 0
                else:
                    user.gradesSum = form.clean_gradesSum()

                user.save()
                serializer = UserSerializer(user)
                return JsonResponse(serializer.data, safe = False)
            else:
                return JsonResponse({'form':'is not valid'}, status=422)

        else:
            user = User.objects.filter(rate = "None")
            serializer = TripSerializer(user, many = True)
            return JsonResponse(serializer.data, safe = False)


class MessagesView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        userId = self.request.query_params.get('userId', None)

        if id is not None:
            return Message.objects.filter(id=id)    
        
        if userId is not None:
            return Message.objects.filter(Q(fromUserId=userId) | Q(toUserId=userId))

        return Message.objects.all()

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)