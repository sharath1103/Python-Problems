word = input("Enter the word: ")
balance_word = input("Enter the char: ")
def balanced_function(word, balance_word):
    lowered_word = word.lower()
    lowered_bal = balance_word.lower()
    if lowered_bal not in lowered_word:
        return False
    return True

result = balanced_function(word, balance_word)
print("The match is ", result)