length_of_list = int(input("Enter the length of the list: "))
numbers = []
for i in range(length_of_list):
    number = int(input("Enter number {}: ".format(i+1)))
    numbers.append(number)
unique_list=[]
for i in numbers:
    if i not in unique_list:
        unique_list.append(i)
print("The list after removing duplicates is: ", unique_list)