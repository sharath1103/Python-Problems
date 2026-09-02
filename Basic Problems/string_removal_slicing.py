word = input("Enter a string: ")
position = int(input("Enter the position of the character to be removed: "))
def remove_character(string, pos):
    if pos < 0 or pos >=len(string):
        return "Position is out of range"
    else:
        return string[pos:]

result = remove_character(word, position)
print("The string after removing the character at position {} is: {}".format(position, result))