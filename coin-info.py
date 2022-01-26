
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def lambda_handler(event, context):
    parameters = event['params']
    tipo = event['tipo']

    with open('api_key.txt', 'r') as file:
        apikey = file.read()

    if tipo == 'price':
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    elif tipo == 'listing':
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    else:
        raise NameError(f'tipo {tipo} nao configurado')

    # parameters = {
    #     'id': str([i for i in ids]).replace('[', '').replace(']', '').replace(' ', ''),
    #     'convert': 'USD'
    # }
    #
    # parameters = {
    #   'start': '1',
    #   'limit': '2000',
    #   'convert': 'USD'
    # }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': apikey,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return data

#
# param = {'params': {'id': '1,2', 'convert': 'USD'}, 'tipo': 'price'}
#
# data = lambda_handler(param, None)
# print(data)
