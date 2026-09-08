lst = ["apple", "pie", "banana", "kiwi", "pear"]
k = 5
res = []
for i in range(len(lst)):
    if len(lst[i]) >= k:
        res.append(lst[i])
print(res)