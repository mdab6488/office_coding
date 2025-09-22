# Exceptions occur during execution of syntactically correct code when an operation fails for some reason. Unlike syntax errors, exceptions can be handled during runtime, allowing your program to respond to unexpected situations rather than crashing completely.

# Example 1: Division by zero
# This will raise a ZeroDivisionError
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

calculate_average([])  # Empty list causes division by zero

# Example 2: Accessing non-existent dictionary keys (common in web development)
# This will raise a KeyError
user_profile = {'name': 'John', 'email': 'john@example.com'}
print(user_profile['age'])  # Key 'age' doesn't exist

# Example 3: Accessing non-existent attributes
# This will raise an AttributeError
from django.http import HttpResponse
response = HttpResponse()
response.nonexistent_method()  # Method doesn't exist

# Example 4: Type errors
# This will raise a TypeError
"25" + 25  # Trying to concatenate string and integer

"""Table: Common Exceptions in Web Development"""

# Exception	Common Web Development Scenario	How to Handle
# KeyError	Accessing missing keys in JSON data or session storage	Use .get() method with default values
# AttributeError	Accessing missing attributes on objects	Use hasattr() or try-except blocks
# TypeError	Incorrect data types in API requests	Validate input data before processing
# ValueError	Invalid data format (e.g., malformed UUID)	Use validation libraries like Pydantic
# ImportError	Missing dependencies in your project	Ensure proper requirements.txt configuration
