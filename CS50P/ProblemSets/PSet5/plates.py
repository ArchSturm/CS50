def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    if 2 <= len(str) <= 6 and str.isalnum():
        n, p = find_first_number(str)
        if n == None:
            return True
        elif n == "0" or p < 2:
            return False
        else:
            while p + 1 < len(str) + 1:
                if str[p].isalpha():
                    return False
                p += 1
        return True
    else:
        return False

def find_first_number(str):
    for l in str:
        if l.isdecimal():
            return l, str.find(l)
    return None, None

if __name__ == "__main__":
    main()