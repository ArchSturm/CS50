import random
n = 0
x = 0

while n < 1:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass

r = random.randint(1, n)

while x != r:
    try:
        x = int(input("Guess: "))
    except ValueError:
        x = 0
    if x < 1:
        continue
    elif x < r:
        print("Too small!")
    elif x > r:
        print("Too large!")
    else:
        print("Just right!")