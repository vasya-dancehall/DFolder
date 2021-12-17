from pandas import Timestamp
import numpy as np
from numba import njit
import numba
import pycurl_requests as requests
import pandas as pd
from pprint import pprint
import sys

sys.path.append(
    "/Users/GlebSokolov/.vscode/extensions/almenon.arepl-2.0.3/node_modules/arepl-backend/python"
)
# from arepl_dump import dump


import time
import numpy as np
import ccxt

symbol = "AGLD-USDT"

exchange = getattr(ccxt, "coinbase")()
since = "2021-10-05 10:00:00"
since_ts = exchange.parse8601(since)
end_ts = since_ts + (3600000)
end = str(pd.to_datetime(end_ts, unit="ms"))

import coinbase
from coinbase.wallet.model import APIObject
from coinbase.wallet.client import Client

coinbase_API_key = "PZsUB9TdWedNjJcu"
coinbase_API_secret = "UP8Jz2cfXvDRdgeeNwFy6fCxfJCkQFea"
client = Client(coinbase_API_key, coinbase_API_secret)
client.get_spot_price(currency="AGLD")
client._make_api_object(client._get("v2", "prices", "AGLD-USD", "historic"), APIObject)

import cbpro
public_client = cbpro.PublicClient()
public_client.get_product_ticker(product_id='AGLD-USD')

ttrades = public_client.get_product_trades(product_id=symbol, before=end_ts, after=since_ts, limit=100)
list(ttrades)
next(ttrades)