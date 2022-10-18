import requests
import os

api_key = os.environ["CURRENCYCONVERSIONAPIKEY"]
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

request = requests.get(url)

data = request.json()

converted_amount = False
last_update = data["time_last_update_utc"]

amount = float(input("Please insert the amount you want to convert: "))

base_currency = input("Type the currency three letter code you want to use as base, type \"available\" to \
check available currencies with USD as base: ")

while base_currency.upper() not in data["conversion_rates"].keys():
    if (base_currency.upper() not in data["conversion_rates"].keys()) and (base_currency.upper() != "AVAILABLE"):
        print("Please insert a valid keyword.")
        base_currency = input("Type the currency three letter code you want to use as base, type \"available\" to \
check available currencies with USD as base: ")
    elif base_currency.upper() == "AVAILABLE":
        print(list(data["conversion_rates"].keys()))
        base_currency = input("Type the currency three letter code you want to use as base, type \"available\" to \
check available currencies with USD as base: ")

new_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency.upper()}"

new_request = requests.get(new_url)

new_data = new_request.json()

last_update = new_data["time_last_update_utc"]

currency = "none"

while currency.upper() not in new_data["conversion_rates"].keys():
    currency = input("Type the currency three letter code you want to convert to, type \"available\" to \
check available currencies: ")
    if (currency.upper() not in new_data["conversion_rates"].keys()) and (currency.upper() != "AVAILABLE"):
        print("Please insert a valid keyword.")
        currency = input("Type the currency three letter code you want to convert to, type \"available\" to \
check available currencies: ")
    elif currency.upper() == "AVAILABLE":
        print(list(new_data["conversion_rates"].keys()))
        currency = input("Type the currency three letter code you want to convert to, type \"available\" to \
check available currencies: ")
    else:
        converted_amount = amount * new_data["conversion_rates"][currency.upper()]
        print(f"The amount to convert was {amount:.2f} {base_currency} and the converted is {converted_amount:.2f} \
in {currency.upper()} at {last_update[:-6]} last updated.")