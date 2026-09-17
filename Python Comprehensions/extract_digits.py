strings = ["abc123", "hello", "42px", "year2024", "no-digits"]
new = [char for s in strings for char in s if char.isdigit()]
print(new)