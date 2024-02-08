

def main():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything?: ").lower().strip()
    if answer_check(answer):
        print("Yes")
    else:
        print("No")

def answer_check(str):

    if str == "42" or str == "forty-two" or str =="forty two":
        return True
    else:
        return False

main()