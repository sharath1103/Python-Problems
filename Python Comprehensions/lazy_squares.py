import sys
import itertools

# Generator expression -- nothing is computed yet
gen = (n ** 2 for n in range(1, 1_000_001))

# Pull only the first 10 values
first_ten = list(itertools.islice(gen, 10))
print("First 10 squares:", first_ten)

# Memory comparison
gen_size  = sys.getsizeof(n ** 2 for n in range(1, 1_000_001))
list_size = sys.getsizeof([n ** 2 for n in range(1, 1_000_001)])

print(f"Generator size:  {gen_size:,} bytes")
print(f"List size:       {list_size:,} bytes")