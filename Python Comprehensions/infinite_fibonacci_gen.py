import itertools
def fibonacci():
    a,b = 1,1
    while True:
        yield a
        a,b = b, a+b
limit = 200
result = list(itertools.takewhile(lambda n:n<limit, fibonacci()))
print(result)