number_of_items = int(input("Enter the number of items: "))
items = []
for i in range(number_of_items):
    item = input("Enter item {}: ".format(i+1))
    items.append(item)
print("Items in the list: ", items)
append_list = input("Enter an item to append to the list: ")
items.append(append_list)
print("Items in the list after appending: ", items)
remove_list = input("Enter an item to remove from the list: ")
if remove_list in items:
    items.remove(remove_list)
    print("Items in the list after removing: ", items)
else:
    print("Item not found in the list")
remove_index = int(input("Enter the index of the item to remove from the list: "))
if remove_index < 0 or remove_index >= len(items):
    print("Index is out of range")
else:
    removed_item = items.pop(remove_index)
    print("Removed item: ", removed_item)
    print("Items in the list after removing by index: ", items)
