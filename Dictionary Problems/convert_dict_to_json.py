import json
person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}
js = json.dumps(person, indent=4)
print(js)