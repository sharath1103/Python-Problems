while True:
    try:
        raw = int(input("Enter the positive number:"))
    except ValueError:
        print("The value is not of int datatype")
        continue
    if raw <=0:
        print("It is a negative number")
        continue
    print("You entered ", raw)
    break
