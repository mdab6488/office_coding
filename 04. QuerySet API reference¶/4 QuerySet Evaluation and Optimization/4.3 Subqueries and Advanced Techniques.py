# Using Subquery and OuterRef
from django.db.models import Subquery, OuterRef
latest_books = Book.objects.filter(author=OuterRef('pk')).order_by('-published_date')
authors = Author.objects.annotate(
    last_pub_date=Subquery(latest_books.values('published_date')[:1])
)  # Annotate each author with their latest publication date :cite[4]

# Using Exists() for subquery existence checks
from django.db.models import Exists
expensive_books = Book.objects.filter(author=OuterRef('pk'), price__gt=100)
authors = Author.objects.annotate(
    has_expensive_books=Exists(expensive_books)
)  # Annotate authors with flag indicating if they have expensive books :cite[4]

# Window functions for advanced analytics
from django.db.models import Window, F, Avg
from django.db.models.functions import RowNumber
books = Book.objects.annotate(
    row_number=Window(expression=RowNumber(), order_by=F('price').desc()),
    avg_price=Window(expression=Avg('price'), partition_by=F('author'))
)  # Add row numbers and average price by author :cite[4]

# Conditional expressions with Case/When
from django.db.models import Case, When, Value, IntegerField
books = Book.objects.annotate(
    price_bucket=Case(
        When(price__lt=50, then=Value('low')),
        When(price__lt=100, then=Value('medium')),
        default=Value('high'),
        output_field=models.CharField(),
    )
)  # Categorize books into price buckets