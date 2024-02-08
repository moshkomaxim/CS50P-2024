def main():
    amount_due = amount()
    print_change(amount_due)

def amount():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        insert_coin = int(input("Insert Coin: "))
        if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
            amount_due = amount_due - insert_coin
    return amount_due

def print_change(n):
    print("Change Owed:", abs(n))


main()
