lst = [1, 2, 3, 4]
new_lst = []
cum_sum = 0
for i in lst:
    cum_sum += i 
    new_lst.append(cum_sum)
print(new_lst)