list_a = [1, 2, 3, 4, 5, 3, 2]
list_b = [3, 4, 5, 6, 7, 4, 5]
new = {n for n in list_a if n in list_b}
print(new)