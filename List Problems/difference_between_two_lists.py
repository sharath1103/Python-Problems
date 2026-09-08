lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6]
for i in lst1:
    if i in lst2:
        lst1.remove(i)
print(lst1)