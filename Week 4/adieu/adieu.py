def main():
    names = get_input()
    print_names(names)


def get_input():
    names = []
    while True:
        try:
            name = input("Name: ").strip().title()
            names.append(name)
        except EOFError:
            print("\n", end = "")
            return names


def print_names(names):
    if len(names) == 1:
        str = f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        str = f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        str = f"Adieu, adieu, to "
        for i in range(len(names) - 1):
            str += names[i] + ", "
        str += f"and {names[-1]}"
    print(str)


main()