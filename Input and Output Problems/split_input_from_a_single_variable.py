values = input("Enter values separated by spaces: ")
values_list = values.split()
for i in range(len(values_list)):
    print("Name {}: {}".format(i+1, values_list[i]))
