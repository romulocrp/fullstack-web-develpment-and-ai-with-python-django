import requests
import os

amount = float(input("Please insert the amount of USD you want to convert: "))

currency = input("Type the currency three letter code you want to convert to, type \"available\" to \
check available currencies: ")

api_key = os.environ["CURRENCYCONVERSIONAPIKEY"]
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

request = requests.get(url)

data = request.json()

converted_amount = False
last_update = data["time_last_update_utc"]

while converted_amount == False:
    if (currency.upper() not in data["conversion_rates"].keys()) and (currency.upper() != "AVAILABLE"):
        print("Please insert a valid keyword.")
        currency = input("Type the currency three letter code you want to convert to, type \"available\" to \
check available currencies: ")
    elif currency.upper() == "AVAILABLE":
        print(data["conversion_rates"].keys())
        currency = input("Type the currency three letter code you want to convert to, type \"available\" to \
check available currencies: ")
    else:
        converted_amount = amount * data["conversion_rates"][currency.upper()]
        print(f"The amount to convert was {amount} USD and the converted is {converted_amount} in {currency.upper()} at \
{last_update[:-6]} last update")