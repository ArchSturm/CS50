items = dict()

while True:
    try:
        item = input().upper()
    except EOFError:
        break
    items[item] = items.get(item, 0) + 1

"""
d.items() returns a list of tuples.
sorted() sorts this list, looking in the first item of the tuple by default,
which is what I want, since it's the key.
dict() creates a new dictionary with the tuples as key, value, now sorted.
https://docs.python.org/3/howto/sorting.html
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
"""
sorted_items = dict(sorted(items.items()))
for k, i in sorted_items.items():
    print(i, k)