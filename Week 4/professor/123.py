import random


def main():

    level = get_level()
    questions = 10
    lives = 3
    score = 0
    while questions > 0:
        num1, num2, suum = generate_integer(level)
        while lives > 0:
            guess = get_input(num1, num2)
            if guess != suum:
                print("EEE")
                lives -= 1
                continue
            score += 1
            break

        if lives != 3:
            print(f"{num1} + {num2} = {suum}")
            lives =3
        questions -= 1
    print(F"Score: {score}")


def get_input(num1, num2):
    while True:
        guess = input(f"{num1} + {num2} = ")
        try:
            guess = int(guess)
            return guess
        except ValueError:
            return guess

def get_level():
    while True:
        try:
            level = input("Level:")
            level = int(level)
        except ValueError:
            continue

        if level < 1:
            continue
        elif level > 3:
            continue
        else:
            return level

def generate_integer(level):
    if level == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        return num1, num2, (num1 + num2)

    if level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        return num1, num2, (num1 + num2)

    if level == 3:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
        return num1, num2, (num1 + num2)


if __name__ == "__main__":
    main()