# Comparative lookups enable filtering based on value relationships:

# Greater than
Product.objects.filter(price__gt=1000)

# Greater than or equal to
Product.objects.filter(price__gte=1000)

# Less than
Product.objects.filter(price__lt=500)

# Less than or equal to
Product.objects.filter(price__lte=500)

# Range between values (inclusive)
from datetime import date
Product.objects.filter(
    release_date__range=(date(2023, 1, 1), date(2023, 12, 31))
)

# These lookups are essential for numeric filtering and date range queries. The range lookup is particularly useful for selecting values within a specified range, including both endpoints.

