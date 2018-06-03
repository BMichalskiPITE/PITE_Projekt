from django import forms
from .models import User
from pprint import pprint


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'mail',
            'id', 
            'username',
            'imageUrl',
            'is_guide',
            'gradesNumber',
            'gradesSum',
            )

class AnnounceUserForm(forms.Form):
    mail = forms.CharField(max_length = 200,required=False)
    id = forms.CharField(max_length = 200,required=False)
    username = forms.CharField(max_length =200,required=False)
    imageUrl = forms.CharField(max_length = 500,required=False)
    is_guide = forms.BooleanField(required=False)
    gradesNumber = forms.IntegerField(required=False)
    gradesSum = forms.IntegerField(required=False)

    def clean_mail(self):
        data = self.cleaned_data['mail']
        return data

    def clean_id(self):
        data = self.cleaned_data['id']
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        return data

    def clean_imageUrl(self):
        data = self.cleaned_data['imageUrl']
        return data

    def clean_is_guide(self):
        data = self.cleaned_data['is_guide']
        return data

    def clean_gradesNumber(self):
        data = self.cleaned_data['gradesNumber']
        return data

    def clean_gradesSum(self):
        data = self.cleaned_data['gradesSum']
        return data