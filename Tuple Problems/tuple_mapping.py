numbers = (1, 2, 3, 4, 5, 6)
new = tuple(filter(lambda x: x is not None, map(lambda x: x if x%2==0 else None ,numbers)))
print(new)
