import getpass
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Login failed. Please check your username and password.")
