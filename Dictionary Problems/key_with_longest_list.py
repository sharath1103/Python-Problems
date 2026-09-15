data = {"fruits": ["apple", "banana", "cherry"], "vegs": ["carrot"], "grains": ["rice", "wheat"]}
longest = max(data.items(), key = lambda item : len(item[1]))[0]
print(longest)