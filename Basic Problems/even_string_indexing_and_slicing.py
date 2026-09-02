word = input("Enter a word: ")
length = len(word)
for i in range(length):
    if i%2==0:
        print(word[i])