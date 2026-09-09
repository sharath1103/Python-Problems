try:
    a = int(input("Enter the number: "))
    print("The number entered is ",a)
except ValueError:
    print("The value entered is not int datatype")