def func1(*args):
    print("The number of arguments passed is:", len(args))
    for arg in args:
        print(arg)
result = func1(1, 2, 3, 4, 5)
result = func1("Hello", "World", "Python")