from datetime import date

class CurrencyConverter:

    rates_dict = {"GBP": 0.90571, "JPY": 146.54, "BRL": 5.29147, "ARS": 150.827}
    request_moment = date.today()

    def __init__(self, amount=None, currency=None):

        self.amount = amount
        self.currency = currency

    def amount_input(self):
        self.amount = float(input("Insert the amount of USD for conversion: "))
        while self.amount < 0:
            print("Value lower than 0, please insert a positive value.\n")
            self.amount = float(input("Insert the amount of USD for conversion: "))
        return self.amount

    def currency_input(self):
        self.currency = input("Insert the currency to convert to (Available: GBP, JPY, BRL, ARS): ").upper()
        while self.currency not in CurrencyConverter.rates_dict:
            print("Input not in the currency database. Please enter one available.\n")
            self.currency = input("Insert the currency to convert to (Available: GBP, JPY, BRL, ARS): ").upper()
        return self.currency

    def print_converted_amount(self):
        converted_amount = self.amount * CurrencyConverter.rates_dict[self.currency]
        return f"The converted amount is: {converted_amount:.2f} {self.currency} at\
 {CurrencyConverter.request_moment.month}/{CurrencyConverter.request_moment.day}/{CurrencyConverter.request_moment.year}."

if __name__=="__main__":
    cc = CurrencyConverter()
    cc.amount_input()
    cc.currency_input()
    print(cc.print_converted_amount())