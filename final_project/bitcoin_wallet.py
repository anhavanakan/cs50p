import csv
import wallet
import gui
import argparse


def main():
    parser = argparse.ArgumentParser(description="Buy and sell bitcoins")
    parser.add_argument("--reset", "-r", action="store_true")
    parser.add_argument("--add", "-a", type=float)
    args = parser.parse_args()
    if args.reset:
        reset_my_wallet()
    if args.add:
        increase_usd_amount(args.add)
    open_wallet()



def increase_usd_amount(amount_of_usd_to_add=1000):

    with open("data.csv", "r") as data_file:
        reader = csv.DictReader(data_file)
        for r in reader:
            bitcoins = float(r['bitcoins'])
            usd = float(r['usd'])
    if (usd + amount_of_usd_to_add) > 1000000000: #billion
        return None


    with open("data.csv", "w") as data_file:
        writer = csv.DictWriter(data_file, fieldnames=["bitcoins", "usd"])
        writer.writeheader()
        writer.writerow({"bitcoins": bitcoins, "usd": usd+amount_of_usd_to_add})


def reset_my_wallet():
    with open("data.csv", "w") as data_file:
        writer = csv.DictWriter(data_file, fieldnames=["bitcoins", "usd"])
        writer.writeheader()
        writer.writerow({"bitcoins": 0, "usd": 1000000})


def get_balance():
    with open("data.csv", "r") as data_file:
        reader = csv.DictReader(data_file)
        for r in reader:
            bitcoins = float(r['bitcoins'])
            usd = float(r['usd'])

        balance = (wallet.Wallet().get_bitcoin_price() * bitcoins) + usd
        return balance

def open_wallet():
    gui.Wallet_GUI()



if __name__ == '__main__':
    main()
