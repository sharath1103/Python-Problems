codes = {"USD": "US Dollar", "EUR": "Euro", "GBP": "British Pound", "JPY": "Japanese Yen"}
new = {v:k for k,v in codes.items()}
print(new)