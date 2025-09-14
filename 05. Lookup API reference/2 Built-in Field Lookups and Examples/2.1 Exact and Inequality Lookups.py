# Django provides numerous built-in lookups that cover most common query scenarios. These lookups can be chained together to create complex queries.

# Exact lookups are the most fundamental type of field comparison:
# Exact match (case-sensitive)
Product.objects.filter(name__exact="Laptop")

# Case-insensitive exact match
Product.objects.filter(name__iexact="laptop")

# Not equal comparison (custom implementation)
Product.objects.filter(name__ne="Laptop")  # ne = not equal

# The exact lookup is case-sensitive and translates directly to SQL's = operator, while iexact performs case-insensitive matching. The ne lookup (not equal) demonstrates how custom lookups can extend Django's functionality.
