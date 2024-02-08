def main():
    string = input("Type string: ")
    print(slowdown(string))

def slowdown(str):
    return str.replace(" ", "...")

main()


