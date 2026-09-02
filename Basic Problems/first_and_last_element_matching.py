number = int(input("Enter a number: "))
list_of_numbers = []
for i in range(number):
    value = int(input("Enter value {}: ".format(i+1)))
    list_of_numbers.append(value)
def first_and_last_element_matching(lst):
    if lst[0] == lst[-1]:
        return True
    else:
        return False
result = first_and_last_element_matching(list_of_numbers)
if result:
    print("The first and last elements of the list are matching.")
else:
    print("The first and last elements of the list are not matching.")
