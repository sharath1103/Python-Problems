original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
inverted = {}
for k, v in original.items():
    inverted.setdefault(v,[]).append(k)
print(inverted)