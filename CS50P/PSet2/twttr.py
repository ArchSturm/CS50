str = input("Input: ")
print("Output: ", end="")
for l in str:
    if l.lower() not in ["a", "e", "i", "o", "u"]:
        print(l, end="")
print()