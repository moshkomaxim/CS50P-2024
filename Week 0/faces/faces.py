def main():
    string = input("Type string: ")
    print(convert(string))

def convert(str):
    str = str.replace(":)", "\U0001F642")
    str = str.replace(":(", "\U0001F641")
    return str

main()