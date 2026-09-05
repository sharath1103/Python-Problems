sentence = input("Enter the sentence: ")
substring = sentence.split("-")
print("The words without hypens are")
for i in range(len(substring)):
    print(substring[i])