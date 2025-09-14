# Q objects are particularly useful for building dynamic queries where conditions may vary based on user input or other factors     

from django.db.models import Q

def build_product_query(categories=None, min_price=None, max_price=None, in_stock_only=False):
    """Build dynamic query based on parameters"""
    query = Q()
    
    if categories:
        query &= Q(category__in=categories)
    
    if min_price is not None:
        query &= Q(price__gte=min_price)
        
    if max_price is not None:
        query &= Q(price__lte=max_price)
        
    if in_stock_only:
        query &= Q(stock__gt=0)
        
    return query

# Usage
query = build_product_query(
    categories=['electronics', 'books'],
    min_price=10,
    max_price=100,
    in_stock_only=True
)
products = Product.objects.filter(query)