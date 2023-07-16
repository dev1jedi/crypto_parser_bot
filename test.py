import requests
from py_currency_converter import convert
import json

#print(convert(base='USD', amount=1000, to=["RUB"])["RUB"])


#
data = {
    "all_coins": [
        {
            "crypto": "BTC",
            "last_price": ""
        }
#         # {
#         #     "crypto": "ETH",
#         #     "last_price": ""
#         # },
#         # {
#         #     "crypto": "XMR",
#         #     "last_price": ""
#         # }
     ]
}




with open("last_price.json") as f:
    dat = json.load(f)

dat["all_coins"][0]["last_price"] = "3938383"

with open("last_price.json", "w") as out:
    json.dump(dat, out)

# print("BTDCNDSD"[:3])


