import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    am = {"12": "00", "1": "01", "2": "02", "3": "03", "4": "04", "5": "05", "6": "06", "7": "07", "8": "08", "9": "09", "10": "10", "11": "11"}
    pm = {"12": "12", "1": "13", "2": "14", "3": "15", "4": "16", "5": "17", "6": "18", "7": "19", "8": "20", "9": "21", "10": "22", "11": "23"}
    start, end = s.split(" to ")
    start = conv_parts(start, am, pm)
    end = conv_parts(end, am, pm)
    return f"{start} to {end}"


def conv_parts(part, am, pm):
    if matches := re.search(r"^(\d{1,2})(:\d{2})? (A|P)M", part):
        hr = matches.group(1)
        ap = matches.group(3)
        if min := matches.group(2):
            min = min[1:]
        else:
            min = "00"
        if int(hr) <= 0 or int(hr) > 12:
            raise ValueError
        elif int(min) < 0 or int(min) > 59:
            raise ValueError
        elif ap == "A":
            hr = am[hr]
        elif ap == "P":
            hr = pm[hr]
        return f"{hr}:{min}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()