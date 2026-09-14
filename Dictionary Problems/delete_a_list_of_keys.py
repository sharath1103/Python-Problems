product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
keys_to_remove = ["stock", "warehouse"]
for keys in keys_to_remove:
    product.pop(keys,None)
print(product)