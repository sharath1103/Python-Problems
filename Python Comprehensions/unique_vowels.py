sentence = "the quick brown fox jumps over the lazy dog"
vowels = "aeiouAEIOU"
new = {sentence[i] for i in range(len(sentence)) if sentence[i] in vowels}        
print(new)