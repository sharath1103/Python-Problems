items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
seen = set()
result = set()
for i in items:
    if i not in seen:
        result.add(i)
    else:
        seen.add(i)
print(result)
