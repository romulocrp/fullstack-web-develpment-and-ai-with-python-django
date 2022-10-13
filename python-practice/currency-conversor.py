amount = float(input("Insert the amount of USD for conversion: "))

currency = input("Insert the currency to convert to (Available: GBP, JPY, BRL, ARS): ").upper()

rates_dict = {"GBP": 0.90571, "JPY": 146.54, "BRL": 5.29147, "ARS": 150.827}

converted_amount = amount * rates_dict[currency]

print(f"The converted amount is: {converted_amount:.2f} {currency} at 10/13/2022.")