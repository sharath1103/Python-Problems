list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0
for i in range(len(list1)):
    if list1[i] == target:
        count+=1
print(target,"occured",count, "times.")