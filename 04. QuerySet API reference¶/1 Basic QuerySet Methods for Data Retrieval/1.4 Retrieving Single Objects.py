# The get() method returns exactly one object. It raises exceptions if no object or multiple objects are found.

# Get a specific author
author = Author.objects.get(name="Sunil Nepali")  # Only if exactly one exists :cite[4]

# Get with multiple parameters
book = Book.objects.get(title="Sample title", price=100)

# Using primary key
member = Member.objects.get(pk=1)

# Note: Always use get() when you expect exactly one result. For cases where you might have multiple results, use filter() instead 