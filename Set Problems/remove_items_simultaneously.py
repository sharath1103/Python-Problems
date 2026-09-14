items = {10, 20, 30, 40, 50, 60}
to_remove = {20, 40, 60}
items.difference_update(to_remove)
print(items)
