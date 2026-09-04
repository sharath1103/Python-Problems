def outer_function(a,b):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    def inner_function(a,b):
        print("The sum of the two numbers is:", a + b + 5)
    inner_function(a, b)
result = outer_function(0, 0)