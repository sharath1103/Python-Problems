lst = [10, 21, 4, 45, 66, 93, 11]
even, odd = 0, 0
for i in lst:
    if i % 2 == 0:
        even +=1
    else:
        odd +=1
print("Even: ", even)
print("Odd: ", odd)