sentence = input("Enter the sentence: ")
new = sentence.split()
result = ""
for i in range(len(new)):
    if len(new[i]) > len(result):
        result = new[i]
print("The longest word is ", result)