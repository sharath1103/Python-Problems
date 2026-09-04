def applyoperation(func, a, b):
    def func(a, b):
        mul = a * b
        add = a + b
        return mul, add
    return func(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = applyoperation(applyoperation, a, b)
print("The product of the two numbers is:", result[0])
print("The sum of the two numbers is:", result[1])