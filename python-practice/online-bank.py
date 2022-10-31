import datetime

class Account:

    def __init__(self, user_name: str, balance: float, statement: dict):
        self.user_name = user_name
        self.balance = balance
        self.statement = statement
        
    def deposit(self, amount: float):
        date = datetime.datetime.now()
        self.balance += amount
        self.statement[f"{date.month}/{date.day}/{date.year} {date.hour}:{date.minute}:{date.second}"] = f"Deposit: {amount}"

    def withdraw(self, amount: float):
        date = datetime.datetime.now()
        self.balance -= amount
        self.statement[f"{date.month}/{date.day}/{date.year} {date.hour}:{date.minute}:{date.second}"] = f"Withdraw: {amount}"
