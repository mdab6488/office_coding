# The input() function reads user input as a string 

"""🔹 Simple Input"""
name = input("Enter your name: ")
print(f"Hello, {name}!")

"""🔹 Type Conversion"""
# Input is always a string, so convert for numerical data:
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
print(f"Next year, you'll be {age + 1} years old.")

# Web Example: Handling form inputs:
# Simulating form data processing
user_input = input("Enter username and email (comma-separated): ")
username, email = user_input.split(',')
print(f"Username: {username.strip()}, Email: {email.strip()}")

"""🔹 Multiple Inputs in One Line"""
# Use split() to process multiple inputs:
data = input("Enter name, age, country: ").split()
name, age, country = data[0], int(data[1]), data[2]
print(f"{name} from {country} is {age} years old.")

# With map():
x, y = map(int, input("Enter two numbers: ").split())
print(f"Sum: {x + y}")

