# QuerySets are lazy - they don't hit the database until they are evaluated. Understanding when evaluation occurs is crucial for optimization 

# No database hit here
queryset = Book.objects.all()

# Database hit occurs here (iteration)
for book in queryset:
    print(book.title)

# Other evaluation triggers:
list(queryset)        # Conversion to list
bool(queryset)        # Boolean test
len(queryset)         # Length check
[book for book in queryset]  # List comprehension

# Avoiding early evaluation with iterator()
large_queryset = Book.objects.all().iterator()
for book in large_queryset:
    print(book.title)  # Efficient for large datasets :cite[4]