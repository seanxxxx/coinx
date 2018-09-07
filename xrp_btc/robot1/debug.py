import requests

eth_usdt_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(52) + '/?convert=usdt'
print(eth_usdt_url)

req = requests.get(eth_usdt_url)
print(req.text)
print(req.json()['data']['quotes']['USDT']['price'])