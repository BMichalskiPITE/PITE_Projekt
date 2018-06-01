from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = (
            'userId',
            'tripName',
            'tripDescription',
            'places',
            )

class AnnounceTripForm(forms.Form):
    userId = forms.CharField(max_length = 200)
    tripId = forms.IntegerField()

    def clean_userId(self):
        data = self.cleaned_data['userId']
        return data

    def clean_tripId(self):
        data = self.cleaned_data['tripId']
        return data

class AcceptTripForm(forms.Form):
    userId = forms.CharField(max_length = 200)
    tripId = forms.IntegerField()
    guideId = forms.CharField(max_length = 200)

    def clean_userId(self):
        data = self.cleaned_data['userId']
        return data

    def clean_tripId(self):
        data = self.cleaned_data['tripId']
        return data

    def clean_guideId(self):
        data = self.cleaned_data['guideId']
        return data