word = input("Enter the word: ")
vowels = "aeiouAEIOU"
count = 0
for i in range(len(word)):
    if word[i] in vowels:
        count += 1
print("The count of vowels in the word {} is {}".format(word,count))