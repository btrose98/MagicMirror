import sys, os
from configparser import ConfigParser
import requests, json

class weatherCall:
    file = "config.ini"
    config = ConfigParser()
    config.read(file)

    #One Call API example - https://openweathermap.org/api/one-call-api
    # https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

    latitude = config['Location']['latitude']
    longitude = config['Location']['longitude']
    units = "metric"
    api_key = config['apiKeys']['openweathermapKey']

    complete_url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={Units}&appid={APIkey}".format(lat=latitude, lon=longitude, Units=units, APIkey=api_key)

    response = requests.get(complete_url)
    data = response.json()

    temp = data["current"]["temp"]
    humidity = data["current"]["humidity"]
    # rain = data["current"]["rain"]["1h"] #in mm
    cloud = data["current"]["clouds"] #in %

    imagePath = os.getcwd() + "/assets/whiteSun.png" 
    # if(rain > 0) : imagePath = os.getcwd() + "/assets/rain.png"
    # elif (cloud > 25) : imagePath = os.getcwd() + "/assets/clouds.png" 
    if (cloud > 20) : imagePath = os.getcwd() + "/assets/clouds.png" 


    # print(temp)
    # print(humidity)
