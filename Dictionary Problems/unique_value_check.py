data = {"a": 1, "b": 2, "c": 3, "d": 2}
new_lst = list(data.values())
if len(new_lst) == len(set(new_lst)):
    print(True)
else:
    print(False)