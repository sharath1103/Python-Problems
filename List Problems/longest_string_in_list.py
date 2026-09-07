lst = ["PHP", "Exercises", "Backend", "Python"]
longest = ""
for i in range(len(lst)):
    if len(lst[i]) > len(longest):
        longest = lst[i]
    else:
        pass
print(longest)