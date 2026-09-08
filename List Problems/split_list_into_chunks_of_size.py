lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
def split_list(lst, n):
    new_list = [lst[x:x+n] for x in range(0, len(lst), n)]
    return new_list
res = split_list(lst,n)
print(res)