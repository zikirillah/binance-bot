import config
import sys
from binance.client import Client

self = Client(config.api_key, config.api_secret)
symbol = sys.argv[1]


def get_balance(asset):
    balance = self.get_asset_balance(asset=asset)
    print(balance)


get_balance(symbol)
