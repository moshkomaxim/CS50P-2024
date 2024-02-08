import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if um_count := len(re.findall(r"(\bum\b)", s.lower())):
        return um_count
    else:
        return 0


if __name__ == "__main__":
    main()