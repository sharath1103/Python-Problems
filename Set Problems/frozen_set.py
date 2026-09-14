try:
    fs = frozenset([1, 2, 3, 4, 5])
    b = {3,4,5}
    print("The intersection: ", fs & b)
    print("trying to add")
    fs.add(8)
except AttributeError, TypeError:
    print("Manipulation operation is not allowed")