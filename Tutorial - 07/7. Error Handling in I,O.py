# Always validate input and handle errors 
"""🔹 Basic Validation"""
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(f"Invalid input: {e}")

"""🔹 File Operation Error Handling"""
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
except IOError as e:
    print(f"I/O Error: {e}")

