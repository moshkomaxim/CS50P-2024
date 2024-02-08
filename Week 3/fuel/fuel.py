def main():
    fraction = get_fraction()
    print_fraction(fraction)


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").strip().split(sep = "/")
            if(int(x) > int(y)):
                continue
            else:
                fraction = int(x) / int(y)
                return round(fraction, 2)
        except (ValueError, ZeroDivisionError):
            pass


def print_fraction(fr):
    if(fr >= 0.99):
        print("F")
    elif(fr <= 0.01):
        print("E")
    else:
        fr = round(fr*100)
        print(f"{fr}%")


main()
