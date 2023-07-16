x, y, z = input("Expression: ").split()
if y == "+":
    r = int(x) + int(z)
    print(f"{r:.1f}")
elif y == "-":
    r = int(x) - int(z)
    print(f"{r:.1f}")
elif y == "*":
    r = int(x) * int(z)
    print(f"{r:.1f}")
elif y == "/":
    r = int(x) / int(z)
    print(f"{r:.1f}")
