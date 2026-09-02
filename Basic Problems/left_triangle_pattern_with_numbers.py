size = int(input("Enter the size of the triangle: "))
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
