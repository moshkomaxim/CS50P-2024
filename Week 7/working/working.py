import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d\d?):?(\d\d?)? (AM|PM) to (\d\d?):?(\d\d?)? (AM|PM)$", s.strip()):
        from_time = {"hh": matches.group(1), "mm": matches.group(2), "type": matches.group(3)}
        to_time = {"hh": matches.group(4), "mm": matches.group(5), "type": matches.group(6)}

        if from_time["mm"] == None and to_time["mm"] == None:
            from_time["mm"] = 0
            to_time["mm"] = 0

        from_time = convertToWorldTime(from_time)
        to_time = convertToWorldTime(to_time)

        return_str = "{:02}:{:02} to {:02}:{:02}".format(from_time["hh"], from_time["mm"], to_time["hh"], to_time["mm"])
        return return_str
    else:
        raise ValueError


def convertToWorldTime(time):
    time["hh"] = int(time["hh"])
    time["mm"] = int(time["mm"])

    if time["hh"] > 12 or time["mm"] > 59:
        raise ValueError

    if time["type"] == "AM":
        if time["hh"] == 12:
            time["hh"] = 0
    elif time["type"] == "PM":
        if time["hh"] < 12:
            time["hh"] += 12

    del time["type"]
    return time


if __name__ == "__main__":
    main()


    #9:00 AM to 5:00 PM
    #9 AM to 5 PM