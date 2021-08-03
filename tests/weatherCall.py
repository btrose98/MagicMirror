import sys
from configparser import ConfigParser
import requests, json

file = "config.ini"
config = ConfigParser()
config.read(file)
print(config.sections())

#One Call API example - https://openweathermap.org/api/one-call-api
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

# Why can't these be converted to float???
latitude = config['Location']['latitude']
longitude = config['Location']['longitude']
units = "metric"
api_key = config['weatherApi']['apiKey']

complete_url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={Units}&appid={APIkey}".format(lat=latitude, lon=longitude, Units=units, APIkey=api_key)

response = requests.get(complete_url)
data = response.json()
print(data["current"])