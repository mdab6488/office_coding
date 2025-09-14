# F() expressions are particularly useful for filtering based on field comparisons without needing to retrieve values into Python 

# Find products where price is greater than discounted price
Product.objects.filter(price__gt=F('discounted_price'))

# Find companies with more employees than chairs
Company.objects.filter(num_employees__gt=F('num_chairs'))

# Find products where inventory is less than reorder threshold
Product.objects.filter(stock__lt=F('reorder_level'))

# Complex comparisons using multiple fields
Product.objects.filter(
    sales__gt=F('initial_stock') * 0.8,
    stock__lt=F('initial_stock') * 0.2
)