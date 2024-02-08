def main():
    date = get_date()
    print_date(date)

def get_date():
    while True:
        try:
            str = input("Date: ").strip()
            date = date_to_dict(str)
            if check_date(date) == True:
                return date
        except (ValueError, IndexError, UnboundLocalError):
            continue
        except EOFError:
            quit()

def date_to_dict(str):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    if str[0].isdigit():
        temp = str.split("/")
    elif str[0].isalpha() and str.index(","):
        temp = str.split(" ")
        temp[1] = temp[1].replace(",", "")
        for i in range(len(months)):
            if temp[0] == months[i]:
                temp[0] = i+1
                break
    date = {"mm" : int(temp[0]), "dd" : int(temp[1]), "yy" : int(temp[2])}
    return date

def check_date(date):
    if date["dd"] <= 31 and 0 < date["yy"] <= 9999 and date["mm"] <= 12:
        return True

def print_date(date):
    print(f"{date['yy']}-{int(date['mm']):02}-{date['dd']:02}")


main()