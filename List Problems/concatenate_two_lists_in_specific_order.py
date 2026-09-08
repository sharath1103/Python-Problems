lst1 = ["Hello ", "Take "]
lst2 = ["Dear", "Sir"]
new_lst = []
word = ""
for i in range(len(lst1)):
    for j in range(len(lst2)):
        word = lst1[i] + lst2[j]
        new_lst.append(word)
print(new_lst)