from binance.client import Client
api_key='yX5TYKRSbJxoNPSNGN7lxRrXiucLlf71goVkMMnynQeMJ0wgOR6TdG1YUVYqIQe9'
api_secret='zrymX840yoUvdWCeQ360v7xatcX0JjkBGWlwgdoAEVyjzBbxizEXtGVitZ8qNlhM'
client = Client(api_key, api_secret)
prices = client.get_all_tickers()
print(prices)