def parse_and_divide(value, divisor):
    try:
        num = float(value)
        div = num / divisor
        print("The divided value is", div)
    except ValueError:
        print("Error:", value, "cannot be converted to number")
    except ZeroDivisionError:
        print("The divisor cannot be zero")

parse_and_divide("10", 2)