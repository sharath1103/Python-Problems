length_of_list = int(input("Enter the length of the list: "))
values = []
for i in range(length_of_list):
    value = int(input("Enter value {}: ".format(i+1)))
    values.append(value)
min_value = min(values)
max_value = max(values)
print("The minimum value in the list is: ", min_value)
print("The maximum value in the list is: ", max_value)