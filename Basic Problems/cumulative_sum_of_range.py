number = int(input("Enter a number: "))
print("Printing current number and previous number in a range of {}".format(number))
for i in range(number):
    sum = 0
    sum += i
    print("Current Number {} Previous Number {} Sum {}".format(i,i-1,sum))


