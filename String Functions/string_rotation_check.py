s1 = input("Enter the word1: ")
s2 = input("Enter the word2: ")
combined = s1 + s2
if len(s1) == len(s2):
    print("Is Rotation: ",s2 in combined)
else:
    print("Length of the text is different")