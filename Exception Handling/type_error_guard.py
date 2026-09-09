def add (a,b):
    try:
        return a+b
    except TypeError:
        print("The arguments passed is not an int datatype")

add(10, "20")
add(10,20)