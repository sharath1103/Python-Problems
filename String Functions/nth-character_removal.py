word = input("Enter the word: ")
index = int(input("Enter the index to remove: "))
print("The word after the removal is ", word[:index] + word[index+1:])