def main():
    str = get_string()
    mod_str = shorten(str)
    print_string(mod_str)


def get_string():
    str = input("Input: ")
    return str

def shorten(word):
    str_tmp = ""
    for i in range(len(word)):
        match word[i].upper():
            case "A" | "E" | "I" | "O" | "U" :
                continue
            case _:
                str_tmp += word[i].upper()
    return str_tmp

def print_string(str):
    print("Output:", str)

if __name__ == "__main__":
    main()
