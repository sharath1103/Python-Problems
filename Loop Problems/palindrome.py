number = 121
temp = number
reverse_num = 0

while number > 0:
    digit = number % 10
    reverse_num = (reverse_num * 10)+ digit
    number = number // 10

if reverse_num == temp:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
    