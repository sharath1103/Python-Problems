lst1 = ["Py", "is", "awes"]
lst2 = ["thon", " ", "ome"]
merged_list = []
merged = ""
if len(lst1) == len(lst2):
    for i in range(len(lst1)):
        merged = lst1[i] +lst2[i]
        merged_list.append(merged)
print(merged_list)