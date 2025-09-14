# Using F() expressions in annotations allows you to create dynamic computed fields directly in your queries .

from django.db.models import Value
from django.db.models.functions import Concat

# Annotate with computed field
companies = Company.objects.annotate(
    chairs_needed=F('num_employees') - F('num_chairs')
)

# Using arithmetic in annotations
products = Product.objects.annotate(
    total_value=F('price') * F('quantity_in_stock')
)

# String concatenation using F() with Value
employees = Employee.objects.annotate(
    full_name=Concat(F('first_name'), Value(' '), F('last_name'))
)

# Conditional annotation using F() with Case/When (explained later)