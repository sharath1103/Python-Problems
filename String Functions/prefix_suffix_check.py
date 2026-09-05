url = input("Enter the url: ")
starting = input("Enter the starting word: ")
ending = input("Enter the last word: ")
print("Is URL Valid: ", url.startswith(starting) and url.endswith(ending))