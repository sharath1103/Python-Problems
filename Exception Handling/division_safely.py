def safe_div(a,b):
    try:
        div = a / b
        print("The result is ",div)
    except ZeroDivisionError:
        print("The denominator (b) value cannot be zero")
    
safe_div(10,0)
safe_div(10,2)