num = 153
num_str = str(num)
power = len(num_str)
total = 0
for digit in num_str:
    total += int(digit) ** power

if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")