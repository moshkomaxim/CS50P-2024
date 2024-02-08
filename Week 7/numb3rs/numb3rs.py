import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    form = "(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])"
    if matches := re.search(f"^{form}\.{form}\.{form}\.{form}$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()