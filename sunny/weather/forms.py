from .models import City
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']

        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
        })}


