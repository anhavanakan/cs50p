import requests


class Wallet:
    def __init__(self, usd=1000000, bitcoins=0):
        self.usd = usd
        self.bitcoins = bitcoins
        self.balance = usd

    def get_bitcoin_price(self):
        response = requests.get(
            "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        )
        data = response.json()
        return float(data["price"])

    def get_balance(self):
        self.balance = self.usd + (self.bitcoins * self.get_bitcoin_price())
        return self.balance

    def is_valid_amount(self, amount):
        try:
            amount = float(amount)
        except:
            raise ValueError("Please specify valid amount.")
        if amount < 0:
            raise ValueError("Please specify valid amount")

    def buy_bitcoin(self, amount=0):
        self.is_valid_amount(amount)
        amount = float(amount)
        if amount > self.usd / self.get_bitcoin_price():
            raise ValueError("Insufficient funds.")
        self.bitcoins += amount
        self.usd -= amount * self.get_bitcoin_price()
        self.balance = self.usd + self.get_bitcoin_price() * self.bitcoins

    def sell_bitcoin(self, amount=0):
        self.is_valid_amount(amount)
        amount = float(amount)
        if self.bitcoins < amount:
            raise ValueError("Not sufficient coins")
        self.bitcoins -= amount
        self.usd += amount * self.get_bitcoin_price()
        self.balance = self.usd + self.get_bitcoin_price() * self.bitcoins

    def __str__(self):
        return f"""\n BTC:  {self.bitcoins:.8f}\n\nCash: ${self.usd:.2f}\n"""
