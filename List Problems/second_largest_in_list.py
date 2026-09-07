lst = [12, 35, 1, 10, 34, 1, 35]
unique_lst = []
for i in lst:
    if i not in unique_lst:
        unique_lst.append(i)
unique_lst.sort(reverse=True)
print("The second largest second element is ", unique_lst[1])