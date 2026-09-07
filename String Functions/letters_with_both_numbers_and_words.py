word = input("Enter the word: ")
new = word.split()
result = []
for i in new:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        result.append(i)
for j in result:
    print(j)