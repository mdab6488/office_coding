# Q objects enable complex queries using OR, AND, and NOT operators.

from django.db.models import Q

# OR queries
expensive_or_berry_books = Book.objects.filter(
    Q(price__gt=1000) | Q(title__contains="berry")  # Books that are expensive OR have "berry" in title :cite[6]
)

# AND queries (implicit)
recent_expensive_books = Book.objects.filter(
    Q(price__gt=100) & Q(published_date__year=2023)  # Books that are expensive AND recent
)

# NOT queries
non_berry_books = Book.objects.filter(~Q(title__contains="berry"))  # Books that don't have "berry" in title :cite[6]

# Complex combinations
complex_query = Book.objects.filter(
    (Q(price__gt=100) | Q(author__name="Sunil")) & ~Q(title__startswith="The")
)  # (Expensive OR by Sunil) AND title doesn't start with "The"

# Combining with exclude()
excluding_query = Book.objects.exclude(
    Q(price__lt=50) | Q(author__age__lt=30)  # Exclude cheap books OR books by authors under 30
)