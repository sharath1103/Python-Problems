list1 = [20, 25, 30, 35, 40]
list2 = [21, 20, 31, 30, 41]
final_list = []
for i in list1:
    if i%2 ==1:
        final_list.append(i)
for j in list2:
    if j%2==0:
        final_list.append(j)
print(final_list)
