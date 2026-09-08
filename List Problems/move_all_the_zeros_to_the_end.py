lst = [0, 1, 0, 3, 12]
zero_lst = []
for i in lst:
    if i == 0:
        zero_lst.append(i)
        lst.remove(i)
print("Final list: ",lst + zero_lst)