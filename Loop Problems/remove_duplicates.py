original = [1, 2, 2, 3, 4, 4, 4, 5]
new_lst = []
for num in original:
    if num not in new_lst:
        new_lst.append(num)
print(new_lst)