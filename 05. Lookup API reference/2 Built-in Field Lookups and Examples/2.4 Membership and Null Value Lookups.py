# Membership lookups allow filtering based on value presence in a collection:

# IN lookup - match any value in a list
Product.objects.filter(category__in=['Electronics', 'Accessories'])

# IS NULL lookup - match null values
Product.objects.filter(description__isnull=True)

# IS NOT NULL lookup
Product.objects.filter(description__isnull=False)

# The in lookup is particularly powerful when combined with querysets:

# Get recent orders
recent_orders = Order.objects.filter(date__gte=date(2023, 9, 1))

# Find products from recent orders
Product.objects.filter(order__in=recent_orders)

# This approach enables complex queries using subqueries and related data