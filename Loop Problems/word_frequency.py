text = "apple banana apple orange banana apple"
words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        # First time seeing this word
        frequency[word] = 1

print(frequency)