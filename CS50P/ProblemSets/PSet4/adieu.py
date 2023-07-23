import inflect

p = inflect.engine()
l = list()
while True:
    try:
        l.append(input("Name: "))
    except EOFError:
        break

mylist = p.join(l)

print("Adieu, adieu, to", mylist)