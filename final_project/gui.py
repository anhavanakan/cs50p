from wallet import Wallet
import tkinter as tk
from tkinter import messagebox
import csv


class Wallet_GUI:
    def __init__(self):
        with open("data.csv") as data_file:
            reader = csv.DictReader(data_file)
            for dict in reader:
                btc = float(dict["bitcoins"])
                usd = float(dict["usd"])
        self.wallet = Wallet(usd, btc)
        self.root = tk.Tk()

        self.root.geometry("800x500")

        self.root.resizable(False, False)
        self.root.title("Bitcoin wallet")

        self.USD_label = tk.Label(
            self.root,
            text=f"USD:      {self.wallet.usd:,.2f}",
            font=("Arial", 20),
            padx=15,
        )
        self.USD_label.place(x=10, y=10)

        self.bitcoin_amount_label = tk.Label(
            self.root,
            text=f"BTC:       {self.wallet.bitcoins:.8f}",
            font=("Arial", 20),
            padx=15,
        )
        self.bitcoin_amount_label.place(x=10, y=50)

        self.balance_label = tk.Label(
            self.root,
            text=f"Total balance ${self.wallet.get_balance():,.2f}",
            font=("Arial", 20),
            padx=15,
        )
        self.balance_label.place(x=370, y=10)

        self.buy_button = tk.Button(
            self.root,
            text="BUY",
            font=("Arial", 20),
            width=10,
            command=lambda: [
                self.update_bitcoin_and_usd_amount_after_buying(),
                self.update_bitcoin_and_usd_in_csv(),
            ],
        )
        self.buy_button.place(x=170, y=320)

        self.sell_button = tk.Button(
            self.root,
            text="SELL",
            font=("Arial", 20),
            width=10,
            command=lambda: [
                self.update_bitcoin_and_usd_amount_after_selling(),
                self.update_bitcoin_and_usd_in_csv(),
            ],
        )
        self.sell_button.place(x=470, y=320)

        self.bitcoin_amount_entry = tk.Entry(self.root, font=("Arial", 18))
        self.bitcoin_amount_entry.place(x=270, y=250)

        self.bitcoin_price_label = tk.Label(
            self.root,
            text=f"${self.wallet.get_bitcoin_price():.2f}",
            font=("Arial", 36),
        )
        self.bitcoin_price_label.place(x=285, y=170)
        self.update_bitcoin_price_and_total_balance_every_second()

        self.__text_price_of_bitcoin_label = tk.Label(
            self.root, text="Bitcoin Price", font=("Arial", 14)
        )
        self.__text_price_of_bitcoin_label.place(x=350, y=140)

        self.root.mainloop()

    def update_bitcoin_price_and_total_balance_every_second(self):
        bitcoin_current_price = self.wallet.get_bitcoin_price()
        self.bitcoin_price_label.config(text=f"${bitcoin_current_price:,.2f}")
        current_balance = self.wallet.get_balance()
        self.balance_label.config(text=f"Total balance: ${current_balance:,.2f}")
        self.root.after(1000, self.update_bitcoin_price_and_total_balance_every_second)

    def update_bitcoin_and_usd_amount_after_buying(self):
        amount_of_BTC = self.bitcoin_amount_entry.get()
        try:
            self.wallet.buy_bitcoin(amount_of_BTC)
            self.bitcoin_amount_label.config(
                text=f"BTC:       {self.wallet.bitcoins:.8f}"
            )
            self.USD_label.config(text=f"USD:      {self.wallet.usd:,.2f}")

        except ValueError as e:
            messagebox.showinfo("", e)


    def update_bitcoin_and_usd_amount_after_selling(self):
        amount_of_BTC = self.bitcoin_amount_entry.get()
        try:
            self.wallet.sell_bitcoin(amount_of_BTC)
            self.bitcoin_amount_label.config(
                text=f"BTC:       {self.wallet.bitcoins:.8f}"
            )
            self.USD_label.config(text=f"USD:      {self.wallet.usd:,.2f}")
        except ValueError as e:
            messagebox.showinfo("", e)

    def update_bitcoin_and_usd_in_csv(self):
        with open("data.csv", "w") as data_file:
            writer = csv.DictWriter(data_file, fieldnames=["bitcoins", "usd"])
            writer.writeheader()
            writer.writerow({"bitcoins": self.wallet.bitcoins, "usd": self.wallet.usd})

if __name__ == "__main__":
    Wallet_GUI()
