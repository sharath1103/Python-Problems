def function_with_keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

result1 = function_with_keyword_arguments(name="Alice", age=20, city="New York")
result2 = function_with_keyword_arguments(country="USA", language="English")
    