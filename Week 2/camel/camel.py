def main():
    string = get_input()

    print_string(string)


def get_input():
    str = input("camelCase: ")
    return str


def print_string(str):
    for c in str:
        if(c.isupper()):
            print("_", end = "")
            print(c.lower(), end = "")
        else:
            print(c, end = "")
    print("\n")

main()