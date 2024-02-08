from emoji import emojize


def main():
    str = input("Input: ").strip()
    print(emojize(str, language="alias"))

main()