groups = [[1, 2, 3], [-1, 4, 5], [6, 7, 8], [0, 9, 10], [-3, -1, 2], [4, 5, 6]]
new = [group for group in groups if all(n > 0 for n in group)]
print(new)