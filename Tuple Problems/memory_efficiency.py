import sys

data = range(1_000_000)
list_data = list(data)
tuple_data = tuple(data)

list_size = sys.getsizeof(list_data)
tuple_size = sys.getsizeof(tuple_data)
diff = list_size - tuple_size

print("List size: ",list_size, "bytes")
print("Tuple size: ",tuple_size, "bytes")
print("Difference: {:.2f}".format(diff), "bytes")