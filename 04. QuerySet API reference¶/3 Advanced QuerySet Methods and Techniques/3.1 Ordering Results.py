# The order_by() method allows you to sort the QuerySet by one or more fields.

# Simple ordering
books_asc = Book.objects.order_by('price')  # Ascending order by price :cite[4]
books_desc = Book.objects.order_by('-price')  # Descending order by price :cite[4]

# Multiple field ordering
books = Book.objects.order_by('author', '-published_date')  # Sort by author ascending, then by published date descending

# Random ordering
random_books = Book.objects.order_by('?')  # Random ordering (can be slow on large datasets)

# Removing default ordering
books_no_order = Book.objects.order_by()  # Remove any default ordering