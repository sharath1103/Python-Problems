import copy

original = {"name": "Alice", "scores": [90, 85, 92]}

# Shallow copy
shallow_copy = original.copy()

shallow_copy["scores"].append(99)

print("Original:", original)
print("Shallow Copy:", shallow_copy)

# Deep copy
deep_copy = copy.deepcopy(original)

deep_copy["scores"].append(100)

print("Original:", original)
print("Deep Copy:", deep_copy)