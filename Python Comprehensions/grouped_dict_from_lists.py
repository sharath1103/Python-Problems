keys = ["name", "age", "city", "email"]
values = ["Alice", 30, None, None]
new = {k: (v if v is not None else "N/A") for k,v in zip(keys,values)}
print(new)