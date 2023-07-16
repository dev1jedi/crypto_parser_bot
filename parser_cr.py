import json
import requests
from py_currency_converter import convert
from decimal import Decimal



class Parser:
    def crypto(self):

        url = "https://api.binance.com/api/v3/ticker/price?symbol="
        text = ""

        with open("last_price.json") as f:
            data = json.load(f)

        coins = data["all_coins"]

        for i in coins:
            usd = url + i["crypto"] + "USDT"
            rub = url + i["crypto"] + "RUB"

            usd_1 = requests.get(usd).json()
            rub_1 = requests.get(rub).json()


            try:
                p_usd = float(Decimal(round(float(usd_1['price']), 3)).normalize())
                p_rub = float(Decimal(round(float(rub_1['price']), 3)).normalize())

                if float(i["last_price"]) > p_usd:
                    text = text + f"🔻 1 {i['crypto']} = {p_usd} USD, {p_rub} RUB" + "\n\n"
                else:
                    text = text + f"🔼 1 {i['crypto']} = {p_usd} USD, {p_rub} RUB" + "\n\n"

                i["last_price"] = p_usd


            except:
                p_usd = float(Decimal(round(float(usd_1['price']), 3)).normalize())
                convet = convert(base='USD', amount=p_usd, to=["RUB"])["RUB"]
                p_rub = float(Decimal(round(float(convet), 3)).normalize())

                if float(i["last_price"]) > p_usd:
                    text = text + f"🔻 1 {i['crypto']} = {p_rub} USD, {p_rub} RUB" + "\n\n"
                else:
                    text = text + f"🔼 1 {i['crypto']} = {p_rub} USD, {p_rub} RUB" + "\n\n"

                i["last_price"] = p_usd

        with open("last_price.json", "w") as ff:
            json.dump(data, ff)


        return text

parser2 = Parser()