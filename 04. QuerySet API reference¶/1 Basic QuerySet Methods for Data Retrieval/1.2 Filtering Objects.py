# The filter() method allows you to retrieve objects that match specific criteria. You can chain multiple filters together or combine them in a single call.

# Single filter
cheap_books = Book.objects.filter(price__lte=300)  # Books priced at or below 300 :cite[4]

# Chained filters
red_berries = Food.objects.filter(name__contains="berry").filter(color="red")  # Red berries :cite[5]

# Multiple filters in one call
red_berries = Food.objects.filter(name__contains="berry", color="red")  # More efficient :cite[5]

# Field lookups
books_with_berry = Book.objects.filter(title__contains="berry")  # Contains "berry" in title
recent_books = Book.objects.filter(published_date__year=2023)  # Books published in 2023