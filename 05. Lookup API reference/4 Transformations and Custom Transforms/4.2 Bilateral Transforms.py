# Bilateral transforms apply the transformation to both sides of the comparison:

from django.db.models import Transform

class UpperCase(Transform):
    lookup_name = 'upper'
    function = 'UPPER'
    bilateral = True  # Apply to both lhs and rhs

# Register for character fields
from django.db.models import CharField, TextField
CharField.register_lookup(UpperCase)
TextField.register_lookup(UpperCase)

# Bilateral transforms ensure consistent transformation of both the field values and the comparison value:

# Case-insensitive comparison using UPPER()
Author.objects.filter(name__upper="doe")

# Generated SQL:
WHERE UPPER("author"."name") = UPPER('doe')

# This approach provides database-agnostic case-insensitive matching without relying on database-specific features
