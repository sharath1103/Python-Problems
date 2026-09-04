n = int(input("Enter a number: "))
lst = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    lst.append(element)
x = list(map(lambda num: num *2, lst))
print("The list of doubled numbers is:", x)