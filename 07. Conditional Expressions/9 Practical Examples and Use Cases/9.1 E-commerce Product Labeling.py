from django.db.models import Case, Value, When

# Categorize products based on price
products = Product.objects.annotate(
    price_label=Case(
        When(price__lt=10, then=Value('cheap')),
        When(price__gte=10, price__lt=50, then=Value('moderate')),
        When(price__gte=50, then=Value('expensive')),
        default=Value('unknown')
    )
)

# Equivalent SQL:
# SELECT *, 
#   CASE 
#     WHEN price < 10 THEN 'cheap'
#     WHEN price >= 10 AND price < 50 THEN 'moderate'
#     WHEN price >= 50 THEN 'expensive'
#     ELSE 'unknown'
#   END AS price_label
# FROM product;

# This example shows how to implement dynamic categorization directly in your database queries, which is useful for e-commerce applications 