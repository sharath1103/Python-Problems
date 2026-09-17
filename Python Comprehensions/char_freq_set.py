sentence = "comprehension makes python powerful"
new = {char for char in sentence if char !=" " and sentence.count(char) > 1}
print(new)