def main():
    grocery_list = {}
    while True:
        try:
            item = get_item()
            if grocery_list.get(item) == None:
                grocery_list.update({item: 1})
            else:
                grocery_list.update({item: grocery_list[item] + 1})
        except EOFError:
            print_list(grocery_list)
            break


def get_item():
    str = input().lower().strip()
    return str


def print_list(list):
    s_list = sorted(list.items())
    for i in range(len(s_list)):
        print(f"{s_list[i][1]} {s_list[i][0].upper()}")


main()