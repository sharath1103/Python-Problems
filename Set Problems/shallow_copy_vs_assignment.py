original = {1, 2, 3, 4, 5}
original1 = {1, 2, 3, 4, 5}

#Assignment
a = original
a.add(99)

print("Original: ", original)
print("Copied: ",a)

#copy

a = original1.copy()
a.add(99)
print("Original (Copy): ",original1)
print("Copied (Copy): ", a)
