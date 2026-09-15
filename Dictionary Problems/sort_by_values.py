scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}
new = dict(sorted(scores.items(), key=lambda item: item[1]))
print(new)