original = {"a": 1, "b": 2, "c": 3}
new = {v :k for k, v in original.items()}
print(new)