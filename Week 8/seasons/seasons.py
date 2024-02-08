from datetime import date
import sys
import re
import inflect


def getDate(my_date):
    try:
        if matches := re.search(r"^(\d+)-(\d+)-(\d+)$", my_date):
            yy = int(matches[1])
            mm = int(matches[2])
            dd = int(matches[3])
            return date(yy, mm, dd)
        else:
            sys.exit("Invalid date")
    except (ValueError, TypeError):
        sys.exit("Invalid date")


def dateToMinutes(my_date):
    minutes = (date.today() - my_date).days * 24 * 60
    return minutes


def printMinutes(minutes):
    p = inflect.engine()
    minutes = (p.number_to_words(minutes, andword="")).capitalize()
    print(f"{minutes} minutes")


def main():
    my_date = input("Date of Birth: ").strip()
    my_date = getDate(my_date)
    minutes = dateToMinutes(my_date)
    printMinutes(minutes)


if __name__ == "__main__":
    main()
