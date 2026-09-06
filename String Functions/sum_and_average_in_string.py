word = input("Enter the word: ")
num = 0
count = 0
for i in range(len(word)):
    if word[i].isdigit():
        num = num + int(word[i])
        count += 1
print("The sum of the value is ", num)
print("The average of the value is {:.2f}".format((num/count)))