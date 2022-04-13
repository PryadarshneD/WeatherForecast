import requests
from pprint import pprint

api_key= 'd3d66e4b99b2308222e2254acdae0403'
city = input("Enter the city name: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?appid"+api_key+"&q="+city
weather_data =requests.get(base_url).json()
pprint(weather_data)