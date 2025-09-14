# You can optimize queries by selecting only specific fields using values() and values_list().

# values() returns dictionaries
book_titles = Book.objects.values('title', 'price')  # Returns list of dictionaries: {'title': '...', 'price': ...} :cite[4]

# values_list() returns tuples
book_titles = Book.objects.values_list('title', flat=True)  # Returns list of titles: ['Book1', 'Book2', ...] :cite[4]

# Specific field filtering with values
expensive_books = Book.objects.filter(price__gt=100).values('title', 'author__name')  # Only get specific fields

# Using only() and defer() for partial loading
books_titles_only = Book.objects.only('title')  # Load only title initially
books_defer_content = Book.objects.defer('description')  # Defer loading large text field