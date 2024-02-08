import random


def main():
    guess_highnum = get_level()
    guess_num = random.randint(1, guess_highnum)
    guessing(guess_num)


def get_level():
    while True:
        try:
            n = int(input("Level: ").strip())
        except ValueError:
            continue
        if n > 0:
                return n


def guessing(num):
    while True:
        try:
            guess = int(input("Guess: ").strip())
        except ValueError:
            continue
        else:
            if guess > num:
                print("Too large!")
            elif guess < num:
                print("Too small!")
            else:
                print("Just right!")
                exit()

                
main()