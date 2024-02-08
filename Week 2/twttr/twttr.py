def main():
    str = get_string()
    mod_str = modify_string(str)
    print_string(mod_str)


def get_string():
    str = input("Input: ")
    return str

def modify_string(str):
    str_tmp = ""
    for i in range(len(str)):
        match str[i].upper():
            case "A" | "E" | "I" | "O" | "U" :
                continue
            case _:
                str_tmp += str[i]
    return str_tmp

def print_string(str):
    print("Output:", str)


main()
