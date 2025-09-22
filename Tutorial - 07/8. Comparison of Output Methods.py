# Below is a quick reference table for choosing the right output method:

"""
Method	Use Case	Example
print() with sep	Simple spaced output	print(a, b, sep=', ')
F-strings	Modern string formatting with expressions	f"Value: {x:.2f}"
str.format()	Complex formatting with reusable templates	"{} + {} = {}".format(a, b, a+b)
%-formatting	Legacy code compatibility	"Name: %s" % name
Manual alignment	Table-like column output	print(f"{name:<10}{age:>5}")
"""