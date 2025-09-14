# Using F() expressions in update operations provides performance benefits and helps avoid race conditions by executing operations directly at the database level .

# Incrementing a counter for all records
Product.objects.update(view_count=F('view_count') + 1)

# Decrementing stock quantity
Product.objects.filter(id=1).update(stock=F('stock') - 1)

# Updating based on another field
Product.objects.update(total_value=F('price') * F('quantity'))

# Multiple field updates in a single query
Product.objects.filter(discontinued=False).update(
    price=F('price') * 1.1,  # Increase price by 10%
    last_updated=Now()
)