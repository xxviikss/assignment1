import requests
import json
n = int(input())
n_list =[]
from pycoingecko import CoinGeckoAPI

cg  = CoinGeckoAPI()
n_list = cg.get_supported_vs_currencies();
for i in range(n):
    print(cg.get_coins_markets(vs_currency='usd')[i])