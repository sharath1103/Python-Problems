matrix = [[10, 20], [30, 40], [50, 60]]
target = 30
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print("The target {} is found at Row: {} and Column: {}".format(target,i,j))
        else:
            pass
