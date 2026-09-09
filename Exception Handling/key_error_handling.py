capitals = {
    "France" : "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilio"
}

try:
    country = input("Enter the country: ")
    capital = capitals[country]
    print("The capital city of ", country, "is ",capital)
except KeyError:
    print("The country", country, "has not found")