# https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from configparser import ConfigParser

#coin ids on coin market cap
bitcoinId = '1'
ethereumId = '1027'
cardanoId = '2010'

currency = 'CAD'

class cryptoCall:
    file = "config.ini"
    config = ConfigParser()
    config.read(file)

    apiKey = config['apiKeys']['coinmarketcapKey']

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'slug':'bitcoin,ethereum,cardano',
    'convert':currency
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apiKey,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    btc = data['data'][bitcoinId]['name'] + ":  $" + str(round(data['data'][bitcoinId]['quote'][currency]['price'], 2)) + " " + currency + "\n"
    eth = data['data'][ethereumId]['name'] + ":  $" + str(round(data['data'][ethereumId]['quote'][currency]['price'], 2)) + " " + currency + "\n"
    ada = data['data'][cardanoId]['name'] + ":  $" + str(round(data['data'][cardanoId]['quote'][currency]['price'], 2)) + " " + currency + "\n"
