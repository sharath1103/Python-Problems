global_variable = 10
print("Before calling the function, global_variable is:", global_variable)
def modify_global_variable():
    global global_variable
    global_variable = 20
    return global_variable

result = modify_global_variable()
print("After calling the function, global_variable is:", global_variable)