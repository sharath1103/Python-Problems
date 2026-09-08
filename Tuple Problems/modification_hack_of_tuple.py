colours = ("red", "green", "blue")

print(colours)

lst = list(colours)

word = "green"

for i, x in enumerate(lst):
    if word in x:
        lst[i] = "yellow"

new_tup = tuple(lst)

print(new_tup)