first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

new = first_set & second_set

print("The intersection element: ", new)

first_set.difference_update(new)
print("After removing elements: ", first_set)

