def process_data(value):
    try:
        return int(value)
    except ValueError as e:
        print("[log] process failed:", e)
        raise
try:
    process_data("abc")
except ValueError as e:
    print("[main] process failed:",e)