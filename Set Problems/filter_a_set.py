numbers = {1, 2, 3, 6, 7, 9, 12, 14, 15}
new_numbers = set()
for i in numbers:
    if i % 3 == 0:
        new_numbers.add(i)
print(new_numbers)