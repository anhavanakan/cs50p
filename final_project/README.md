# BITCOIN WALLET
## Video Demo:  <https://www.youtube.com/watch?v=pE51fzHVzPQ>
## Description:
This is a simulator, where you can buy/sell Bitcoin at real time price without real money.

## Usage
python bitcoin_wallet.py [--add N] [--reset]

Will open the wallet, where you can buy and sell bitcoin at real-time price.

## Arguments
--add  >  will add specified amount of USD to your balance. Max is billion.

--reset > will reset your balnce to 0 BTC and  $1.000.000 USD




## Features

* The Bitcoin Wallet simulator displays the current Bitcoin price in real-time and allows users to buy or sell Bitcoin using virtual money.

* Users can add money to their balance by specifying an amount in USD (up to a maximum of one billion USD).

* Users can reset their balance to 0 BTC and $1,000,000 USD.

* The user's data, including their USD and Bitcoin amounts, are saved in a CSV file.

* The simulator uses the Binance API to get the current Bitcoin price every second, ensuring that the displayed price is always up-to-date.

* The simulator has a graphical user interface (GUI) created using the tkinter module in Python.

## Benefits

* The Bitcoin Wallet simulator is a great tool for people who are new to Bitcoin trading. It allows them to experiment with buying and selling Bitcoin without risking any real money.

* The simulator uses real-time Bitcoin prices, which can help users get a better understanding of how Bitcoin prices fluctuate.

* The simulator is easy to use and has a user-friendly interface.

* The simulator's use of a CSV file to store user data means that it is easy to back up and restore user data if necessary.
