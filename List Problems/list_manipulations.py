lst = [100, 50, 400, 500]
lst[1] = 200
print("Updated (Change): ",lst)
lst.append(600)
print("Updated (Append): ",lst)
lst.insert(2,300)
print("Updated (Insert): ",lst)
lst.remove(600)
print("Updated (Remove 600): ",lst)
lst.pop(0)
print("Updated (Remove Index 0): ",lst)