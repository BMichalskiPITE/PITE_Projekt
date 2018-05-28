from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = (
            'photoRef',
            'placeId',
            'vicinty',
            'latitude',
            'longitude',
            )
    name = forms.CharField(max_length = 200)

    def clean_name(self):
        return self.cleaned_data['name']