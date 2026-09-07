lst = [5, 20, 15, 20, 25, 50, 20]
item_to_remove = 20
lst1 = []
for i in range(len(lst)):
    if item_to_remove != lst[i]:
        lst1.append(lst[i])
print("Cleaned list: ",lst1)