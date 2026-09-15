words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]
new = {}
for i in words:
    letter = i[0]
    new.setdefault(letter,[]).append(i)
print(new)