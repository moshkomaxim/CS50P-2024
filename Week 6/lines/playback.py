#program for replace spaces to three dots

def main():
    string = input("Type string: ")
    print(slowdown(string))


#replace function
def slowdown(str):
    return str.replace(" ", "...")


main()


