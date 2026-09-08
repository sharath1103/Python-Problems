nested = (1, (2, 3), (4, (5, (6, 7))))
lst = list(nested)
def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

res = deep_flatten(lst)
res_tuple = tuple(res)
print(res_tuple)