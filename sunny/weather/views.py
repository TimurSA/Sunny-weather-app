import requests
import json
from django.shortcuts import render

from .forms import CityForm
from .models import City

API_KEY = '0f3882bf52a41954bdfab64b2a5e553f'


def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    city_info = {}

    for city in cities:
        url_weather = f"https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid={API_KEY}"
        response = requests.get(url_weather).json()
        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }
        all_cities.append(city_info)

    url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={cities}&limit=5&appid={API_KEY}"
    # response = requests.get(url_city)
    # data = response.json()
    # lat = data[2]['lat']
    # lon = data[2]['lon']
    # print(response.text)


    contex = {
        'all_info': all_cities, 'form':form
    }

    return render(request, 'weather/index.html', contex)

