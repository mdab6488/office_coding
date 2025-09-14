"""
Lookup	Description	Example
gt	Greater than	Book.objects.filter(price__gt=100)
gte	Greater than or equal	Book.objects.filter(price__gte=100)
lt	Less than	Book.objects.filter(price__lt=100)
lte	Less than or equal	Book.objects.filter(price__lte=100)
"""
# Price range filtering
medium_priced_books = Book.objects.filter(price__gt=100, price__lte=500)  # Books between 100 and 500

# Date comparisons
from django.utils import timezone
published_books = Book.objects.filter(published_date__lte=timezone.now())  # Books published in the past or today