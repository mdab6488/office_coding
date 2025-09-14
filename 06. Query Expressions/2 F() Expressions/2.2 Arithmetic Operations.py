# Django supports various arithmetic operations with F() expressions including addition, subtraction, multiplication, division, modulo, and power operations 

# Find companies with at least twice as many employees as chairs
Company.objects.filter(num_employees__gt=F('num_chairs') * 2)

# Calculate needed chairs for each company
companies = Company.objects.annotate(chairs_needed=F('num_employees') - F('num_chairs'))

# Complex arithmetic operations
Product.objects.update(
    discounted_price=F('price') * (1 - F('discount_percentage') / 100)
)

# Using power operations
Product.objects.update(price_squared=F('price') * F('price'))