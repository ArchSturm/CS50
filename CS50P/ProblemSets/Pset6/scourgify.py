import sys
import csv

temp_list = list()
temp_dict = dict()

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments ")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments   ")
elif sys.argv[1].strip().endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file, fieldnames=["name", "house"])
            for row in reader:
                if len(row["name"].split(", ")) > 1:
                    last, first = row["name"].split(", ")
                    temp_dict = {"first": first, "last": last, "house": row["house"]}
                    temp_list.append(temp_dict)                    
    except FileNotFoundError:
        sys.exit("Could not read", sys.argv[1])
else:
    sys.exit("Not a CSV file")

with open(sys.argv[2], "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    with open("students2.csv", "a") as file:
        for i in temp_list:
            writer.writerow(i)
