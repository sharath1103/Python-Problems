s1 = input("Enter the string 1: ")
s2 = input("Enter the string 2: ")

result = ""

for i in range(min(len(s1), len(s2))):
    result = result + s1[i]
    result = result + s2[len(s2) - 1 - i]

if len(s1) > len(s2):
    result = result + s1[len(s2):]
elif len(s2) > len(s1):
    result = result + s2[:len(s2) - len(s1)]

print("The final combined word is:", result)