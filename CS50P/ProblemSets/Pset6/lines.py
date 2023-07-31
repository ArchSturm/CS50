import sys

count = 0
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments ")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments   ")
elif sys.argv[1].strip().endswith(".py"):
    try:
        with open(sys.argv[1]) as file:
            for line in file.readlines():
                if line.strip().startswith("#") or line.strip() == "":
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")
print(count)