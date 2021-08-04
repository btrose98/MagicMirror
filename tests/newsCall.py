from configparser import ConfigParser
import requests, json

class newsCall:
    file = "config.ini"
    config = ConfigParser()
    config.read(file)

    # https://newsapi.org/docs/get-started
    #100 requests per day

    api_key = config['apiKeys']['newsKey']

    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey={apiKey}').format(apiKey = api_key)
    response = requests.get(url)
    data = response.json()

    articleTitle1 = data["articles"][0]["title"]
    articleTitle2 = data["articles"][1]["title"]
    articleTitle3 = data["articles"][2]["title"]
