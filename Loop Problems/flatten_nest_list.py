nested_list = [[10, 20], [30, 40], [50, 60]]
new = []
for i in nested_list:
    for j in i:
        new.append(j)
print(new)