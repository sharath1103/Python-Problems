try:
    Set_of_tuples = {(1, 2), (3, 4), (5, 6)}
    Set_of_lists = {[1,2], [3,4], [5,6]}
    print(Set_of_tuples)
    print(Set_of_lists)
except TypeError:
    print("Error: ", TypeError)
