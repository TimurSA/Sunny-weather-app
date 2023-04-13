import requests
import json

API_KEY='0f3882bf52a41954bdfab64b2a5e553f'

city = 'Ufa'
url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}"
response=requests.get(url_city)
print(response.text)
data = response.json()
for el in data:
    print(el)
lat = data[2]['lat']
lon = data[2]['lon']
url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
print(lat)
print(lon)
response = requests.get(url_weather)
print(response.text)
data=response.json()
print(data)