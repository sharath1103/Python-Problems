xs = [1, 2, 3]
ys = ["a", "b", "c"]
new = [(x,y) for x in xs for y in ys]
print(new)