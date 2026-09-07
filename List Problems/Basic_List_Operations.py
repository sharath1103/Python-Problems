num = int(input("Enter the number of elements: "))
lst=[]
for i in range(num):
    elements = int(input("Enter the elements: "))
    lst.append(elements)
print("The third element of the list: ", lst[2])
print("The length of the list: ", len(lst))
print("Is the list empty? ", len(lst)==0)