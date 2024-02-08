import sys
from os.path import splitext
from PIL import Image
from PIL import ImageOps


def main():
    r_file, w_file = getFileNames()
    mergePictures(r_file, w_file)


def getFileNames():
    lenght = len(sys.argv)
    if lenght > 3:
        sys.exit("Too many command-line arguments")
    elif lenght < 3:
        sys.exit("Too few command-line arguments")

    str1 = sys.argv[1].lower()
    str2 = sys.argv[2].lower()
    if checkExtension(str1) != True or checkExtension(str2) != True:
        sys.exit("Invalid output")
    elif checkSameExtension(str1, str2) != True:
        sys.exit("Input and output have different extensions")

    return sys.argv[1], sys.argv[2]


def checkExtension(str):
    ok_extensions = [".jpg", ".jpeg", ".png"]
    for extension in ok_extensions:
        if str.endswith(extension):
            return True


def checkSameExtension(str1, str2):
    ext1 = splitext(str1)[1]
    ext2 = splitext(str2)[1]
    if ext1 == ext2:
        return True


def mergePictures(picture_file, new_picture_file):
    try:
        picture = Image.open(picture_file)
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")

    picture = ImageOps.fit(picture, shirt.size)
    picture.paste(shirt, shirt)
    picture.save(new_picture_file)


main()