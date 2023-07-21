months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
day = 0
month = 0
year = 0
while True:
    inp = input("Date: ").split()
    if inp[0].isalpha():
        try:
            month = months.index(inp[0].capitalize()) + 1
        except ValueError:
            continue
        else:
            if inp[1].find(",") == -1:
                continue
            else:
                day = int(inp[1].strip(","))
                year = int(inp[2])
    else:
        inp = inp[0].split("/")
        try:
            month = int(inp[0])
            day = int(inp[1])
            year = int(inp[2])
        except (IndexError, ValueError):
            continue
    if  day > 31 or day < 1 or month > 12 or month < 1 or year < 1:
        continue
    else:
        break
print(f"{year:04}", "-", f"{month:02}", "-", f"{day:02}", sep="")