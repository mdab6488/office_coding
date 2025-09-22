"""🔹 Column Alignment"""
# Use string methods for tabular data 
headers = ["Name", "Age", "Country"]
data = [("Alice", 30, "USA"), ("Bob", 25, "UK"), ("Charlie", 35, "Canada")]

print(f"{headers[0]:<10} {headers[1]:<5} {headers[2]:<10}")
for name, age, country in data:
    print(f"{name:<10} {age:<5} {country:<10}")
    
# Output:
# Name       Age   Country   
# Alice      30    USA       
# Bob        25    UK        
# Charlie    35    Canada    

"""🔹 Using repr() for Debugging"""
# repr() shows unambiguous representation of objects :
s = 'Hello\nWorld'
print(str(s))   # Output: Hello
               #          World
print(repr(s)) # Output: 'Hello\nWorld'
