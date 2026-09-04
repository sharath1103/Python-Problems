n = int(input("Enter an integer: "))
while n > 0:
    reverse_digit = n % 10
    n = n // 10
    print(reverse_digit, end="")
