# The exclude() method returns a QuerySet containing objects that do not match the given lookup parameters.

# Exclude specific records
expensive_books = Book.objects.exclude(price__lt=100)  # Books priced 100 or more :cite[4]

# Multiple exclusions
non_indian_mumbai_users = User.objects.filter(country='India').exclude(city='Mumbai')  :cite[9]

# Complex exclusion using Q objects
from django.db.models import Q
excluded_books = Book.objects.exclude(Q(price__lt=100) | Q(title__contains="berry"))  # Exclude cheap OR berry books