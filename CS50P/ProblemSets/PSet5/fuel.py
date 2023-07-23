def main():
    p = convert(input("Fraction: "))
    s = gauge(p)
    print(s)

def convert(fraction):
    x, y = fraction.split("/")
    p = int(x) / int(y) * 100
    if p > 100:
        raise ValueError
    return int(round(p))


def gauge(p):
    if p >= 99:
        return "F"
    elif p <= 1:
        return "E"
    else:
        return f"{p}%"


if __name__ == "__main__":
    main()