def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check1(s) and check2(s) and check3(s) and check4(s):
        return True
    else:
        return False


def check1(s):
    if s[0:2].isalpha():
        return True
    else:
        return False


def check2(s):
    if 6 >= len(s) >= 2:
        return True
    else:
        return False


def check3(s):
    num_lock = False
    for i in range(len(s)):
        if s[i].isdigit() and num_lock == False:
            if s[i] == "0":
                return False
            else:
                num_lock = True
        elif (s[i].isalpha() and num_lock == True):
            return False

    return True


def check4(s):
    if s.isalnum():
        return True
    else:
        return False


if __name__ == "__main__":
    main()