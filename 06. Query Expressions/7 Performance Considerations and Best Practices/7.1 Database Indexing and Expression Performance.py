# When using expressions in filters, consider database indexing strategies to maintain performance 
# Expressions in filters may not use indexes efficiently
# This might not use an index on price:
Product.objects.filter(price__gt=F('cost_price') * 2)

# Better to create computed fields or indexes where possible
# Consider database-generated columns for frequently used expressions

# For ordering, be aware of performance implications
Company.objects.order_by(Length(F('name')).desc())  # May be slow on large datasets