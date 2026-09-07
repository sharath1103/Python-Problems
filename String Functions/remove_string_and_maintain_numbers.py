word = input("Enter the word: ")
new = ""
for i in range(len(word)):
    if word[i].isdigit():
        new += word[i]
print("The digits are ", int(new))