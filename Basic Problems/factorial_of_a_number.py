number = int(input("Enter a number: "))
factorial = 1
if number < 0:
    print("Enter a positive number")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The factorial of {} is {}".format(number, factorial))