import requests
import sys
import json

def main():
    btc_num = input_num()
    btc_price = get_btc_price()
    print_price(btc_num, btc_price)


def input_num():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too much command-line arguments")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    return n


def get_btc_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except (requests.RequestException, requests.ConnectionError):
        sys.exit("Connection error")
    response = response.json()
    price = response["bpi"]["USD"]["rate_float"]
    return price


def print_price(num, price):
    total = price * num
    print(f"${total:,.4f}")


main()