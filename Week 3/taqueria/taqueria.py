def main():
    sum = 0
    while True:
        try:
            item = get_item()
        except EOFError:
            exit()
        else:
            sum += check_item(item)
            print(f"Total: ${sum:.2f}")


def get_item():
    return input("Item: ").strip().title()


def check_item(item):
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    if item in menu:
        return menu[item]
    else:
        return 0


main()
