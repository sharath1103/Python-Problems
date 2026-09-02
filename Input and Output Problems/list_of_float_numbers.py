number = int(input("Enter an integer: "))
list_of_floats=[]
for i in range(number):
    float_number = float(input("Enter float number {}: ".format(i+1)))
    list_of_floats.append(float_number)
print("The list of float numbers is: ", list_of_floats)