lst = [10, 20, 30, 40, 50]
insert_after = 30
new_item = 35
index = lst.index(insert_after)
lst.insert(index+1,new_item)
print(lst)