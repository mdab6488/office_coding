# Conditional expressions allow you to implement if...elif...else logic directly within your database queries using Case and When classes 

from django.db.models import Case, When, Value, IntegerField, CharField

# Simple case expression for labeling products by price
products = Product.objects.annotate(
    price_label=Case(
        When(price__lt=10, then=Value('cheap')),
        When(price__gte=10, price__lt=50, then=Value('moderate')),
        When(price__gte=50, then=Value('expensive')),
        default=Value('unknown'),
        output_field=CharField()
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