word = input("Enter the string: ")
length = len(word)
new = ""
for i in range(length):
    if word[i].isalnum() or word[i] == " ":
        new = new + word[i]
    else:
        new = new + "#"
print("The corrected word is ",new)