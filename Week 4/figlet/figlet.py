import sys
import pyfiglet
from random import choice


def main():
     font = get_font()
     string = get_string()
     print_figlet(string, font)


def get_font():
    argv_len = len(sys.argv)
    if argv_len == 1:
        font = choice(pyfiglet.FigletFont.getFonts())
    elif argv_len == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font"):
        if sys.argv[2] in pyfiglet.FigletFont.getFonts():
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
         sys.exit("Invalid usage")

    return font


def get_string():
    string = input("Input: ").strip()
    return string


def print_figlet(string, font):
    figlet = pyfiglet.Figlet(font=font)
    print("Output:")
    print(figlet.renderText(string))


main()
