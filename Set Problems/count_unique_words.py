text = "the cat sat on the mat the cat"
new = list(text.split(" "))
new_set = set(new)
print("The number of unique words is", len(new_set))