word = input("Enter the word: ")
digit, alpha, symbols = 0,0,0
for i in range(len(word)):
    if word[i].isdigit():
        digit+=1
    elif word[i].isalpha():
        alpha+=1
    else:
        symbols+=1
print("The word has {} alphabets, {} digits and {} symbols".format(alpha, digit, symbols))