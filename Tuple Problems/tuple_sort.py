students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))
sort_tuple = tuple(sorted(students, key = lambda x : x[1], reverse=False))
print(sort_tuple)
