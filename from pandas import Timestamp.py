from pandas import Timestamp
import numpy as np
from numba import njit
import numba
import pycurl_requests as requests
import pandas as pd
from pprint import pprint

import sys; sys.path.append('/Users/GlebSokolov/.vscode/extensions/almenon.arepl-2.0.3/node_modules/arepl-backend/python')
from arepl_dump import dump
import time
import numpy as np
import ccxt
import coinbase, cbpro
from coinbase.wallet.model import APIObject
from coinbase.wallet.client import Client

symbol = 'AGLD-USDT'
exchange = getattr(ccxt, "coinbase")()
since = "2021-10-05 10:00:00"
since_ts = exchange.parse8601(since)
end_ts = since_ts + (3600000)
end = str(pd.to_datetime(end_ts, unit="ms"))


coinbase_API_key = "PZsUB9TdWedNjJcu"
coinbase_API_secret = "UP8Jz2cfXvDRdgeeNwFy6fCxfJCkQFea"
client = Client(coinbase_API_key, coinbase_API_secret)
client.get_spot_price(currency="AGLD")


import cbpro

public_client = cbpro.PublicClient()
public_client.get_product_ticker(product_id="AGLD-USD")
data = public_client.get_product_historic_rates(
    start=since, end=end, product_id="AGLD-USDT", granularity=60
)
data = pd.DataFrame(data, columns=["time", "low", "high", "open", "close", "volume"])
data["time_iso"] = pd.to_datetime(data["time"], unit="s")


ttrades = public_client.get_product_trades(
    product_id=symbol, before=end_ts/1000, after=since_ts/1000, limit=100
)

print(help(public_client.get_product_trades))
