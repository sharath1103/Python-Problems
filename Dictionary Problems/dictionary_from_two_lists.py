keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]

new = {}

for i in range(len(keys)):
    new[keys[i]] = values[i]

print(new)

new1 = dict(zip(keys,values))
print(new1)