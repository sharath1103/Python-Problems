scores = {"Alice": 82, "Bob": 45, "Charlie": 91, "Diana": 37, "Eve": 55, "Frank": 49}
new = {k:v for k,v in scores.items() if v > 50}
print(new)