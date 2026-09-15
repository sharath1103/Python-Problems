user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
keys = ["id", "username", "email"]
subset = {k: user[k] for k in keys}
print(subset)