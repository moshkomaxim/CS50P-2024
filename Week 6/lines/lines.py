import sys

def main():
    #sys.argv.append("playback.py")
    file_name = get_file_name()
    file_data = get_file_content(file_name)
    code_lines = calc_code_lines(file_data)
    print_result(code_lines)


def get_file_name():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")

    return sys.argv[1]


def get_file_content(name):
    try:
        with open(name) as file:
            f_data = file.readlines()
        return f_data
    except FileNotFoundError:
        sys.exit("File does not exist")


def calc_code_lines(f_data):
    code_lines = 0
    for line in f_data:
        if line.isspace() or line.strip().startswith("#"):
            continue
        else:
            code_lines += 1

    return code_lines


def print_result(code_lines):
    print(code_lines)


main()