def main():
    greeting = input("Greeting: ")
    code = value(greeting)
    if code == 0:
        print("$0")
    elif code == 20:
        print("$20")
    elif code == 100:
        print("$100")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting == "hello" or greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()