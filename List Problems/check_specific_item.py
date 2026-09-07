lst = ["Laptop", "Mouse", "Monitor", "Keyboard"]
target = "Tablet"
res = True
if target in lst:
    res = True
    print("Is {} in inventory? {}".format(target,res))
else:
    res = False
    print("The {} is not in inventory? {}".format(target,res))