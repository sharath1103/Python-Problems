scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}
val = max(scores, key=scores.get)
print("Largest value is in", val)