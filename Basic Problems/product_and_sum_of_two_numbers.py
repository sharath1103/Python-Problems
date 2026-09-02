def product_and_sum(a, b):
    result = 0
    if a*b <=1000:
        result = a*b
    else:
        result = a+b
    return result

a = input("Enter first number: ")
b = input("Enter second number: ")
product_sum_result = product_and_sum(int(a), int(b))
print("The result is:", product_sum_result)