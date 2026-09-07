s1 = input("Enter the word1: ")
s2 = input("Enter the word2: ")
s1_sort = s1.lower()
s2_sort = s2.lower()
res = True
if sorted(s1_sort) == sorted(s2_sort):
    res = True
    print("Are anagram: ", res)
else:
    res = False
    print("Not an anagram")