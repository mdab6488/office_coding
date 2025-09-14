# Q objects enable complex query logic using logical operators (| for OR, & for AND, ~ for NOT) that go beyond simple filtering 

from django.db.models import Q

# OR query: find products that are out of stock OR priced above $100
products = Product.objects.filter(Q(stock=0) | Q(price__gt=100))

# AND query: find products that are in stock AND have discounted price below $50
products = Product.objects.filter(Q(stock__gt=0) & Q(discounted_price__lt=50))

# NOT query: find products that are not discontinued
products = Product.objects.filter(~Q(discontinued=True))

# Complex combination of conditions
products = Product.objects.filter(
    (Q(category='electronics') | Q(category='appliances')) &
    ~Q(price__lt=50) &
    Q(stock__gt=0)
)