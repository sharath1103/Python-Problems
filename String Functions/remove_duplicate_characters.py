word = input("Enter the word: ")
seen = set()
result = []
for char in word:
    if char not in seen:
        result.append(char)
        seen.add(char)
res_str = "".join(result)
print("Original: ", word)
print("Cleaned: ", res_str)
