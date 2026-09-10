nums = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    first_element = nums.pop(0)
    nums.append(first_element)
print(nums)