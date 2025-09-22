"""🔹 F-Strings (Formatted String Literals)"""
# F-strings offer a concise way to embed expressions inside strings 
name = "Bob"
age = 25
print(f"{name} is {age} years old.")  # Output: Bob is 25 years old.

"""Advanced Formatting:"""
import math
price = 99.9876
print(f"Price: ${price:.2f}")                    # Output: Price: $99.99
print(f"Pi: {math.pi:.3f}")                      # Output: Pi: 3.142
print(f"Hex: {255:x}")                           # Output: Hex: ff

# Web Development Example: Generating HTML content:
user = {'name': 'Alice', 'role': 'Admin'}
html_line = f"<div class='user'>{user['name']} <span>({user['role']})</span></div>"
print(html_line)  # Output: <div class='user'>Alice <span>(Admin)</span></div>

"""🔹 str.format() Method"""
# This method uses placeholders {} for formatting 
print("{}'s score is {}".format('Alice', 95))     # Output: Alice's score is 95
print("{1} comes after {0}".format('A', 'B'))     # Output: B comes after A

# Named Arguments:
print("Name: {name}, Age: {age}".format(name='Bob', age=30))

# Web Context: SQL query formatting:
query = "SELECT * FROM users WHERE name={name} AND status={status}".format(name='Alice', status='active')
print(query)  # Output: SELECT * FROM users WHERE name=Alice AND status=active


"""🔹 Legacy %-Formatting"""
# Older method similar to C's printf:
print("Name: %s, Age: %d" % ("Charlie", 28))     # Output: Name: Charlie, Age: 28
print("Decimal: %05d, Float: %.2f" % (3, 3.14159)) # Output: Decimal: 00003, Float: 3.14
