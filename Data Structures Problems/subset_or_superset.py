first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is a subset of second set", first_set.issubset(second_set))
print("Second set is a subset of first set", second_set.issubset(first_set))

print("First set is a superset of second set", first_set.issuperset(second_set))
print("Second set is a superset of first set", second_set.issuperset(first_set))

print("Set", first_set.clear())
print("Second set", second_set)