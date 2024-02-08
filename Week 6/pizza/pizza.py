import sys
import csv
from tabulate import tabulate


def main():
    file_name = getFileName()
    getFileContent(file_name)
    file_data = getFileContent(file_name)
    printMenu(file_data)


def getFileName():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].strip().endswith(".csv") == False:
        sys.exit("Not a CSV file")

    return sys.argv[1]


def getFileContent(file_name):
    file_content = []
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            for line in reader:
                file_content.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")

    return file_content


def printMenu(file_data):
    headers = file_data[0]
    print(tabulate(file_data[1:], headers, tablefmt="grid"))


main()