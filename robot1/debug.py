import random

import requests

eth_usdt_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(52) + '/?convert=usdt'
print(eth_usdt_url)

req = requests.get(eth_usdt_url)
print(req.text)
print(req.json()['data']['quotes']['USDT']['price'])

lastPrice = 0.0774688179
minusNum = lastPrice-lastPrice*random.uniform(0.0001,0.001)
addNum = lastPrice+lastPrice*random.uniform(0.0001,0.001)
price = round(random.uniform(minusNum,addNum),6)

print(minusNum,addNum,price)