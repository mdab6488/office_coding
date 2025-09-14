# Django provides powerful methods for working with related objects: select_related() for foreign key relationships and prefetch_related() for many-to-many and reverse relationships.

# select_related() for foreign key relationships (SQL JOIN)
books_with_author = Book.objects.select_related('author').all()  # Efficiently fetches author info for each book :cite[4]

# prefetch_related() for many-to-many and reverse relationships
authors_with_books = Author.objects.prefetch_related('book_set').all()  # Efficiently fetches books for each author :cite[4]

# Prefetching with filters
from django.db.models import Prefetch
recent_books = Book.objects.filter(published_date__year=2023)
authors = Author.objects.prefetch_related(
    Prefetch('book_set', queryset=recent_books, to_attr='recent_books')
)  # Prefetch only recent books

# Complex prefetching
authors_with_expensive_books = Author.objects.prefetch_related(
    Prefetch('book_set', queryset=Book.objects.filter(price__gt=100), to_attr='expensive_books')
)