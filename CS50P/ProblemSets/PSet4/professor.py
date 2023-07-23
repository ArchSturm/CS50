import random


def main():
    level = get_level()
    fase = 10
    point = 0
    while fase > 0:
        error_count = 0
        x = generate_integer(level)
        y = generate_integer(level)
        s = x + y
        while True:
            print(x, "+", y, "= ", end="")
            try:
                i = int(input())
            except ValueError:
                print("EEE")
                error_count += 1
            else:
                if i == s:
                    point += 1
                    break
                else:
                    print("EEE")
                    error_count += 1
            if error_count == 3:
                print(x, "+", y, "=", s)
                break
        fase -= 1
    print("Score:", point)


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level not in levels:
                raise ValueError
        except ValueError:
            continue
        else:
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()