# Syntax errors, also known as parsing errors, occur when Python cannot interpret your code due to violations of Python's grammatical rules. These errors must be fixed before the code can run successfully.

# Example 1: Missing colon in compound statements
# This will raise a SyntaxError
if True
    print("Hello world")

# Correct version:
if True:
    print("Hello world")

# Example 2: Missing parentheses in function calls (common in Python 3)
# This will raise a SyntaxError
print "Hello world"

# Correct version:
print("Hello world")

# Example 3: Unclosed brackets or quotes
# This will raise a SyntaxError
my_list = [1, 2, 3]
my_string = "Hello"

# Correct version:
my_list = [1, 2, 3]
my_string = "Hello"

# In web development, syntax errors often occur when:
# Quickly prototyping new features

# Working with complex string formatting for HTML templates

# Defining complex data structures like JSON responses
