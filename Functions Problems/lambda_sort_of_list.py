n = int(input("Enter a number: "))
lst = []
for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    lst.append(element)
x = list(sorted(lst, key=lambda s: s, reverse=False))
print("The sorted list is:", x)