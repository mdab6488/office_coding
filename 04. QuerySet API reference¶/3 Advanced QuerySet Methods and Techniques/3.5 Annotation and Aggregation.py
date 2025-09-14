"""3.5.1 Annotation"""
# annotate() adds calculated fields to each object in the QuerySet.

from django.db.models import Count, Avg, Sum, F, Value
from django.db.models.functions import Concat

# Count books per author
authors = Author.objects.annotate(book_count=Count('book'))  # Adds book_count field to each author :cite[4]

# Complex annotations
authors = Author.objects.annotate(
    total_value=Sum('book__price'),  # Total value of all author's books
    avg_price=Avg('book__price'),  # Average book price
    full_name=Concat('first_name', Value(' '), 'last_name')  # Concatenate first and last name
)

# Using F() expressions for field comparisons
books = Book.objects.annotate(
    profit=F('price') - F('production_cost'),  # Calculate profit
    discounted_price=F('price') * 0.9  # Apply 10% discount
)

# Conditional annotations
from django.db.models import Case, When, Value, IntegerField
books = Book.objects.annotate(
    price_category=Case(
        When(price__lt=50, then=Value(1)),
        When(price__lt=100, then=Value(2)),
        default=Value(3),
        output_field=IntegerField(),
    )  # Categorize books by price: 1=cheap, 2=medium, 3=expensive :cite[4]
)

"""3.5.2 Aggregation"""
# aggregate() performs calculations across the entire QuerySet and returns a dictionary of results.

from django.db.models import Avg, Max, Min, Sum, Count

# Basic aggregation
stats = Book.objects.aggregate(
    avg_price=Avg('price'),  # Average price of all books
    max_price=Max('price'),  # Maximum price
    min_price=Min('price'),  # Minimum price
    total_books=Count('id')  # Total number of books
)
# Returns: {'avg_price': 85.5, 'max_price': 200, 'min_price': 10, 'total_books': 150}

# Filtered aggregation
expensive_stats = Book.objects.filter(price__gt=100).aggregate(
    avg_expensive_price=Avg('price'),
    count_expensive=Count('id')
)

# Grouped aggregation
from django.db.models import Avg
author_stats = Author.objects.annotate(book_count=Count('book')).aggregate(
    avg_books_per_author=Avg('book_count')  # Average number of books per author
)

# Multiple aggregations
author_book_stats = Author.objects.aggregate(
    avg_book_price=Avg('book__price'),  # Average book price across all authors
    total_authors=Count('id', distinct=True)  # Count of distinct authors
)

# Table: Common Aggregation Functions and Their Usage
# Function	Description	Example
# Count	Count the number of objects	Count('id')
# Avg	Calculate the average value	Avg('price')
# Sum	Calculate the sum of values	Sum('price')
# Max	Find the maximum value	Max('price')
# Min	Find the minimum value	Min('price')
# StdDev	Calculate standard deviation	StdDev('price')
# Variance	Calculate variance	Variance('price')


""""""