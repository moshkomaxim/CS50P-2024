def print_money(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


def main():
    greeting = input("Greeting: ").lower().strip()
    print_money(greeting)

main()
