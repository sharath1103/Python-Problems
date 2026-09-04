def list_even_numbers(n1, n2):
    list_of_even_numbers = []
    for i in range(n1, n2+1, 2):
        list_of_even_numbers.append(i)
    return list_of_even_numbers

n1 = int(input("Enter the starting number: "))
n2 = int(input("Enter the ending number: "))
even_numbers = list_even_numbers(n1, n2)
print("The list of even numbers between", n1, "and", n2, "is:", even_numbers)