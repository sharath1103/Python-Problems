str1 = input("Enter the word: ")
acronym = "".join([char[0].upper() for char in str1.split()])
print(acronym)