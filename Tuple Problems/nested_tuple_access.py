matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
n = 6
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == n:
            print(n, "is there")
        else:
            pass
