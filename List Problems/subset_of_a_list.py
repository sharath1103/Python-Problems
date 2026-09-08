lst = [1,2,3]
result = [[]]
for element in lst:
    new_subsets = [subset + [element] for subset in result]
    result.extend(new_subsets)
print(result)