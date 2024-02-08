def main():
    str = input("Fraction: ").strip()
    fraction = convert(str)
    fuel = gauge(fraction)
    print(fuel)
    

def convert(fraction):
    x, y = fraction.split(sep = "/")
    fract = int(x) / int(y)
    return fract * 100


def gauge(percentage):
    if(percentage >= 99):
        return "F"
    elif(percentage <= 1):
        return "E"
    else:
        percentage = round(percentage)
        return f"{percentage}%"


if __name__ == "__main__":
    main()
