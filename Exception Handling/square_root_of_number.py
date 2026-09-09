import math
def safe_sqrt(value):
    try:
        number = float(value)
    except ValueError:
        print("The value cannot be converted as number")
    else:
        result = math.sqrt(number)
        print("The sqrt of number is", result)
safe_sqrt("abc")