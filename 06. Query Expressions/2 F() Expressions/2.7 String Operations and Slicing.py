# For string-based fields, Django supports Python's array-slicing syntax with F() expressions (added in Django 5.1) 

# String manipulation using slicing
writer = Writers.objects.get(name="Priyansh")
writer.name = F('name')[1:5]  # Extract substring from index 1 to 4
writer.save()
writer.refresh_from_db()
# writer.name now contains 'riya'

# Potential use cases for string manipulation
User.objects.update(
    email_prefix=F('email')[:F('email').find('@')]  # Not all databases support this
)

# Note: String operations may have limited database support
# and often require using database-specific functions