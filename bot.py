from binance.client import Client
import time

api_key = "TU_API_KEY"
api_secret = "TU_SECRET_KEY"

client = Client(api_key, api_secret)

symbol = "BTCUSDT"

while True:
    price = client.get_symbol_ticker(symbol=symbol)
    print("Precio BTC:", price["price"])
    time.sleep(10)
