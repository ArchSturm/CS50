camel_case = input("camelCase: ")
print("snake_case: ", end="")
for l in camel_case:
    if l.isupper():
        print("_" + l.lower(), end="")
    else:
        print(l, end="")
print()