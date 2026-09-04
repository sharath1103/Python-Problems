n = int(input("Enter a number: "))
lst = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    lst.append(element)
x = list(filter(lambda num: num % 2 == 0, lst))
print("The list of even numbers is:", x)
