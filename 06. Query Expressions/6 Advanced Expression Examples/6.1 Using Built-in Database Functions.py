# Django provides various database functions that can be combined with expressions for powerful queries 

from django.db.models.functions import Upper, Lower, Concat, Length, Coalesce
from django.db.models import Value

# String functions with expressions
Company.objects.annotate(
    upper_name=Upper(F('name')),
    lower_ticker=Lower(F('ticker'))
)

# Concatenation of fields
User.objects.annotate(
    full_name=Concat(F('first_name'), Value(' '), F('last_name'))
)

# Length of string fields
Company.objects.annotate(name_length=Length(F('name')))

# Ordering by expression results
Company.objects.order_by(Length(F('name')).asc())

# Using Coalesce to handle null values
Product.objects.annotate(
    effective_price=Coalesce(F('discounted_price'), F('price'))
)