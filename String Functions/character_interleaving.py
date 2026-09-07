s1 = input("Enter the word1: ")
s2 = input("Enter the word2: ")
new=""
if len(s1) == len(s2):
    for i in range(len(s1)):
        new+=s1[i]
        new+=s2[i]
else:
    print("The strings doesn't have equal length")
print(new)

