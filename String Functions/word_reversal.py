word = input("Enter the word: ")
new = word.split()
reversed_word = new[::-1]
res = " ".join(reversed_word)
print("After reversal: ", res)