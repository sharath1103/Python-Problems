word = input("Enter the word: ")
upper = ""
lower = ""
for i in range(len(word)):
    if word[i].isupper():
        upper = upper + word[i]
    else:
        lower = lower + word[i]
print("The final word is: ", lower + upper)
