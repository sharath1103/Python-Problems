number = float(input("Enter a decimal number: "))
octal_number = oct(int(number))
print("The octal representation of {} is {}".format(number, octal_number[2:]))