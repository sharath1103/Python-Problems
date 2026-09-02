number = int(input("Enter a number: "))
list_of_divisible_items = []
for i in range(number):
    elements = int(input("Enter element {}: ".format(i+1)))
    list_of_divisible_items.append(elements)
divisor = int(input("Enter the divisor: "))
def divisible_items(lst, divisor):
    divisible_list = []
    for item in lst:
        if item % divisor == 0:
            divisible_list.append(item)
    return divisible_list
result = divisible_items(list_of_divisible_items, divisor)
if result:
    print("The items in the list that are divisible by {} are: {}".format(divisor, result))
else:
    print("No items in the list are divisible by {}".format(divisor))