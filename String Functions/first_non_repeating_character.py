str1 = input("Enter the word: ")
word = ""
for i in range(len(str1)):
    if str1.count(str1[i])==1:
        word = str1[i]
        break
print(word)