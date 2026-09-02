## With substring input, the code will find the frequency of the given substring in the word.
word = input("Enter a word: ")
word_to_find = input("Enter the substring to find its frequency: ")
print("The frequency of the substring in the word is:", word.count(word_to_find))

## Without any substring input, the code will find the frequency of all possible characters in the given word.
for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        substring = word[i:j]
        word_frequency = word.count(substring)

if word_frequency > 1:
    print("The character '{}' appears {} times in the word.".format(substring, word_frequency))


## Without any substring input, the code will find the frequency of all possible substrings in the given word.
def words_frequency(word):
    words = word.split()
    for i in words:
        frequency = words.count(i)
        if frequency > 1:
            return i, frequency
    return None, 0

fword, result = words_frequency(word)
if result > 1:
        print("The substring '{}' appears {} times in the word.".format(fword, result))