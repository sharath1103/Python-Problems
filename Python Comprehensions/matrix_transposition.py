matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[matrix[i][j] for i in range(3)]for j in range(3)]
print("Transposed:", transposed)