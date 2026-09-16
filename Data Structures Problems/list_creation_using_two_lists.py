l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd_lst = [l1[i] for i in range(len(l1)) if i%2==1]
even_lst = [l2[i] for i in range(len(l1)) if i%2==0]
print("Final list:", odd_lst + even_lst)