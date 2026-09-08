lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
new_lst = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        new_lst.append(lst[i][j])
print(new_lst)