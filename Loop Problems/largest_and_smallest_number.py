num = 75869
min = 9
max = 0
while num > 0:
    digit = num % 10
    if digit > max:
        max = digit
    if digit < min:
        min = digit
    num = num // 10
print("The Largest Number is",max)
print("The Smallest Number is", min)