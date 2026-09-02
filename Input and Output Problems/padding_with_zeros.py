number = int(input("Enter an integer: "))
print("The padded number with zeros is: {:0>5}".format(number))
print("The padded number with zeros is:", str(number).zfill(5))
