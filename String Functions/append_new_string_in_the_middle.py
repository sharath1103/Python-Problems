s1 = input("Enter the word1: ")
s2 = input("Enter the word2: ")

length_word1 = len(s1)
middle = length_word1 // 2

print("The appended string is:", s1[:middle] + s2 + s1[middle:])