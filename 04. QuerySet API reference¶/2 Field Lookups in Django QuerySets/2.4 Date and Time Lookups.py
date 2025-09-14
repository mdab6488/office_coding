# Django provides powerful date and time lookups for working with datetime fields.

# Year, month, and day lookups
books_2023 = Book.objects.filter(published_date__year=2023)  # Books published in 2023
books_january = Book.objects.filter(published_date__month=1)  # Books published in January

# Date range filtering
from datetime import date
start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)
books_2023 = Book.objects.filter(published_date__range=(start_date, end_date))  # Books published in 2023

# Relative date filtering
from django.utils import timezone
recent_books = Book.objects.filter(published_date__gte=timezone.now() - timezone.timedelta(days=30))  # Books published in last 30 days

# Table: Common Date Lookups and Their Usage
"""
Lookup	Description	Example
year	Exact year match	published_date__year=2023
month	Exact month match	published_date__month=1
day	Exact day match	published_date__day=1
week	Week number	published_date__week=52
week_day	Day of week	published_date__week_day=1
date	Date comparison	published_date__date=date(2023,1,1)
range	Date range	published_date__range=(start, end)
"""
