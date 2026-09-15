text = "the cat sat on the mat the cat"
new_dict = {}
for word in text.lower().split():
    new_dict[word] = new_dict.get(word,0)+1
print(new_dict)