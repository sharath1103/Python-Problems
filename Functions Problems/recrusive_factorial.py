def recrusive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recrusive_factorial(n-1)

n = int(input("Enter a number: "))
result = recrusive_factorial(n)
print("The factorial of", n, "is:", result)