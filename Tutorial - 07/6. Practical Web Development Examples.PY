"""🔹 User Registration Simulation"""
# Simulating user registration form processing
print("=== User Registration ===")
name = input("Full Name: ")
email = input("Email: ")
password = input("Password: ")
age = int(input("Age: "))

print("\n=== Registration Successful ===")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Age: {age}")
print(f"Password: {'*' * len(password)}")

"""🔹 Generating HTML Content"""
# Generating dynamic HTML
users = [("Alice", 30, "Admin"), ("Bob", 25, "Editor")]

html_output = "<table border='1'>\n"
html_output += "<tr><th>Name</th><th>Age</th><th>Role</th></tr>\n"
for name, age, role in users:
    html_output += f"<tr><td>{name}</td><td>{age}</td><td>{role}</td></tr>\n"
html_output += "</table>"

print(html_output)

"""🔹 Reading Configuration Files"""
# Reading and parsing a simple config file
config = {}
with open('config.ini', 'r') as file:
    for line in file:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            config[key] = value

print(f"Database URL: {config.get('db_url', 'Not set')}")
print(f"Debug Mode: {config.get('debug', 'False')}")