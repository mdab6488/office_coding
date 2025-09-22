# The print() function is fundamental for displaying output. It accepts multiple parameters and provides formatting options.

"""🔹 Basic Usage"""

print('Hello, World!')  # Output: Hello, World!
print(42)               # Output: 42

"""🔹 Multiple Arguments"""
# By default, print() separates arguments with a space and ends with a newline:
name = "Alice"
age = 30
print("Name:", name, "Age:", age)  # Output: Name: Alice Age: 30


"""🔹 Using sep and end Parameters"""
# sep specifies the separator between arguments (default: space).
# end specifies the ending character (default: newline).
print('Python', 'is', 'powerful', sep='-')      # Output: Python-is-powerful
print('Hello', end=' ')
print('World!')                                  # Output: Hello World!

# Example in Web Context: Displaying form data:
user_data = ['John Doe', 'john@example.com', 'USA']
print('User:', *user_data, sep=' | ')  # Output: User: John Doe | john@example.com | USA


"""🔹 Basic Usage"""
