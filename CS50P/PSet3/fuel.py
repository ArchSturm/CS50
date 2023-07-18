while True:
    tank = 0
    try:
        x, y = input("Fraction: ").split("/")
        p = int(x) / int(y) * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        tank = tank + p
        if tank > 100:
            continue
        elif tank >= 99:
            print("F")
            break
        elif tank <= 1:
            print("E")
            break
        else:
            print(f"{tank:.0f}", "%", sep="")
            break