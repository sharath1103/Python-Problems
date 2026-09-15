data = {"name": "Alice", "age": None, "city": "Paris", "score": None}
new = {k : v for k,v in data.items() if v != None}
print(new)