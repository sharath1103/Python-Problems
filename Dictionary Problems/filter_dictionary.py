scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
new = {k : v for k,v in scores.items() if v > 60}
print(new)