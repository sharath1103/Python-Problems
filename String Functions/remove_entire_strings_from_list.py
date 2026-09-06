num = int(input("Enter the number of elements in list: "))
lst =[]
for i in range(num):
    elements = input("Enter the element: ")
    lst.append(elements)
final = list(filter(None, lst))
print(final)