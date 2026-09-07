lst = [[1, 2], [3, 4, 5], [6, 7]]
num = 5
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == num:
            print("Accessed ", num)
            break
        else:
            pass