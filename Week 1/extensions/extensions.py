def main():
    file_name = input("Print the name of file: ").lower().strip()
    check_file_type(file_name)

def check_file_type(str):
    if str.endswith(".gif"):
        print("image/gif")
    elif str.endswith(".jpg") or str.endswith(".jpeg"):
        print("image/jpeg")
    elif str.endswith(".png"):
        print("image/png")
    elif str.endswith(".pdf"):
        print("application/pdf")
    elif str.endswith(".txt"):
        print("text/plain")
    elif str.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")



main()