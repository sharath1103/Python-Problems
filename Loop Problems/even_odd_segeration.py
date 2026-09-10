lst = [1, 2, 3, 4, 5, 6]
even_lst = []
odd_lst = []
for i in lst:
    if i % 2 == 0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print(even_lst + odd_lst)