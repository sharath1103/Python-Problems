def expo(base, value):
    if value == 0:
        return 1
    else:
        return base * expo(base, value - 1)

base = int(input("Enter the base: "))
value = int(input("Enter the exponent: "))
result = expo(base, value)
print(f"{base} raised to the power of {value} is: {result}")