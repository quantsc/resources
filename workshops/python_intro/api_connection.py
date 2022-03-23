import requests
import json

print('Using the following API documentation: https://polygon.io/docs/options/get_v2_aggs_ticker__optionsticker__range__multiplier___timespan___from___to')

# # Base request
# url = 'https://api.polygon.io/v2/aggs/ticker/O:TSLA210903C00700000/range/1/day/2021-07-22/2021-07-22?adjusted=true&apiKey=7pRcOcWmBi5kopFcVgryfnJgAb0i1s4K&limit=120&sort=asc'
# res = requests.get(url)
# print('initial request results:\n',json.dumps(res.json(), indent=4))

# Prettier request
headers = {
    'adjusted': True,
    'apiKey': '7pRcOcWmBi5kopFcVgryfnJgAb0i1s4K',
    'limit': 120,
    'sort': 'asc'
}
url = 'https://api.polygon.io/v2/aggs/ticker/O:TSLA210903C00700000/range/1/day/2021-07-22/2021-07-22'
res = requests.get(url, headers)
print('\n\nsame thing: \n', json.dumps(res.json(), indent=4))

resJson = res.json()
print(resJson['ticker'])