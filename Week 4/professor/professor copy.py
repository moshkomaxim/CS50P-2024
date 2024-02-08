import random


def main():
    lvl = get_level()
    problems = generate_integer(lvl)
    score = get_answers(problems)
    print("Score:", score)


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
        except ValueError:
            continue
        else:
            if lvl == 1 or lvl == 2 or lvl == 3:
                return lvl


def generate_integer(level):
    problems = []
    for i in range(10):
        if level == 1:
            n1 = random.randint(1, 9)
            n2 = random.randint(1, 9)
        elif level == 2:
            n1 = random.randint(10, 99)
            n2 = random.randint(10, 99)
        elif level == 3:
            n1 = random.randint(100, 999)
            n2 = random.randint(100, 999)
        problems.append([n1, n2, n1+n2])

    return problems


def get_answers(p_list):
    i = 0
    errors = 0
    attempts = 3
    while i < 10:
        print(f"{p_list[i][0]} + {p_list[i][1]} = ", end = "")
        try:
            answer = int(input())
        except ValueError:
            continue
        else:
            if answer == p_list[i][2]:
                i += 1
            else:
                attempts -= 1
                print("EEE")
                if(attempts == 0):
                    print(f"{p_list[i][0]} + {p_list[i][1]} = {p_list[i][2]}")
                    attempts = 3
                    i += 1
                    errors += 1
    return i - errors


if __name__ == "__main__":
    main()