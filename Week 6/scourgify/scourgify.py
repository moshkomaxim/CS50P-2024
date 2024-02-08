import sys
import csv

def main():
    r_file_name, w_file_name = getFileName()
    file_data = getFileData(r_file_name)
    converted_data = convertFileData(file_data)
    writeFileData(w_file_name, converted_data)


def getFileName():
    len_argv = len(sys.argv)
    if len_argv > 3:
        sys.exit("Too many command-line arguments")
    elif len_argv < 3:
        sys.exit("Too few command-line arguments")
    return sys.argv[1], sys.argv[2]


def getFileData(file_name):
    data = []
    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for line in reader:
                data.append({"name": line["name"], "house": line["house"]})
    except FileNotFoundError:
        #print("Could not read", file_name)
        sys.exit(f"Could not read {file_name}")

    return data


def convertFileData(file_data):
    for line in file_data:
        last, first = line["name"].split(", ")
        line.pop("name")
        line.update({"first": first, "last": last})

    return file_data


def writeFileData(file_name, data):
    with open(file_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in data:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
        sys.exit()


main()