def largest_number_in_list():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i + 1)))
        lst.append(element)
    maximum = max(lst)
    return maximum

result = largest_number_in_list()
print("The largest number in the list is:", result)