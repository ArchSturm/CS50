
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        ip = ip.strip().split(".")
    except ValueError:
        return "False"
    if len(ip) != 4:
        return "False"
    for i in ip:
        try:
            i = int(i)
        except ValueError:
            return "False"
        if i < 0 or i > 255:
            return "False"
        else:
            continue
    return "True"


if __name__ == "__main__":
    main()