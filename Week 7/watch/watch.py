import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if matches := re.search(r'src="https?://(?:www\.)?youtube.com/embed/(\w+)"', s):
        short_url = f"https://youtu.be/{matches.group(1)}"
        return short_url
    else:
        return None


if __name__ == "__main__":
    main()