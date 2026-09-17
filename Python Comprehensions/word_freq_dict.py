words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
new = set(words)
new_dict = {word: words.count(word) for word in new}
print(new_dict)