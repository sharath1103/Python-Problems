def recrusive_addition(n):
    if n == 0:
        return 0
    else:
        return n + recrusive_addition(n - 1)

n = int(input("Enter a number: "))
result = recrusive_addition(n)
print("The sum of numbers from 1 to", n, "is:", result)