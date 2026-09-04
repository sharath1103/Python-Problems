num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
print(f"The reverse of the number is: {reverse}")
if num == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")