import requests
from pprint import pprint
API_key='5c72a3496beea6c7678b0baa2d3b099f'

city = input('enter your city: ')

base_url='http://api.openweathermap.org/data/2.5/weather?&appid='+API_key+'&q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)

