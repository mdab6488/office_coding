"""
Lookup	Description	Example
contains	Case-sensitive containment test	Book.objects.filter(title__contains='berry')
icontains	Case-insensitive containment test	Book.objects.filter(title__icontains='berry')
startswith	Case-sensitive starts-with	Book.objects.filter(title__startswith='The')
istartswith	Case-insensitive starts-with	Book.objects.filter(title__istartswith='the')
endswith	Case-sensitive ends-with	Book.objects.filter(title__endswith='berry')
iendswith	Case-insensitive ends-with	Book.objects.filter(title__iendswith='berry')
"""
# Finding books with specific string patterns
berry_books = Book.objects.filter(title__contains="berry")  # Contains "berry" :cite[5]
the_books = Book.objects.filter(title__istartswith="the")  # Starts with "the" (case-insensitive)

# Complex string filtering
from django.db.models import Q
berry_or_nut_books = Book.objects.filter(Q(title__contains="berry") | Q(title__contains="nut"))  # Contains "berry" OR "nut"