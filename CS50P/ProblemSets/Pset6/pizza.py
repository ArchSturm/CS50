import sys
import csv
from tabulate import tabulate

count = 0
table = list()
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments ")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments   ")
elif sys.argv[1].strip().endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)        
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a CSV file")

print(tabulate(table, headers="keys", tablefmt="grid"))
