items = ["apple", "banana", "cherry"]
n = 5
try:
    value = items[n]
    print("The value in the index {} is {}".format(n,value))
except IndexError:
    print("The index is out of range since the value of the list is ",len(items))