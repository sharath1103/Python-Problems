value = "Loops are Fun!"
vowels = "aeiouAEIOU"
v = 0
c = 0
for i in range(0,len(value)):
    if value[i].isalpha() and value[i] in vowels:
        v += 1
    elif value[i].isalpha() and value[i] not in vowels:
        c +=1
    else:
        pass
print("The number of vowels is",v)
print("The number of consonants is",c)