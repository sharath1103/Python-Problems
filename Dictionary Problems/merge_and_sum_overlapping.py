dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}
merged = dict1.copy()
for k,v in dict2.items():
    merged[k] = merged.get(k,0)+v
print(merged)