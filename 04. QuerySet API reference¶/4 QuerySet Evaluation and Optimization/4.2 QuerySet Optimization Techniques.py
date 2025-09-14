# Use select_related() for foreign keys
books = Book.objects.select_related('author')  # Single query with JOIN

# Use prefetch_related() for many-to-many and reverse relations
authors = Author.objects.prefetch_related('books')  # Additional query for related objects

# Use only() and defer() for large fields
books = Book.objects.only('title', 'author__name')  # Load only specified fields
books = Book.objects.defer('description')  # Defer large text fields

# Use values()/values_list() for specific fields
book_data = Book.objects.values('title', 'author__name')  # Returns dicts instead of models

# Use count() instead of len() for counting
total_books = Book.objects.count()  # Efficient SQL COUNT

# Use exists() for existence checks
has_books = Book.objects.exists()  # Efficient existence check
has_expensive_books = Book.objects.filter(price__gt=100).exists()

# Use update() for bulk updates
Book.objects.filter(price__lt=100).update(price=120)  # Single UPDATE query :cite[4]

# Use bulk_create() for bulk creation
books = [Book(title=f"Book {i}", price=i*10) for i in range(100)]
Book.objects.bulk_create(books)  # Efficient bulk creation :cite[4]

# Use select_for_update() for locking in transactions
from django.db import transaction
with transaction.atomic():
    book = Book.objects.select_for_update().get(id=1)
    book.price += 10
    book.save()  # Locks row until transaction completes :cite[4]