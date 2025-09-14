# Understanding when expressions are evaluated can help you write more efficient queries .

# QuerySets are lazy - no database hit until evaluation
q = Company.objects.annotate(chairs_needed=F('num_employees') - F('num_chairs'))
q = q.filter(chairs_needed__gt=0)  # Still no database hit
results = list(q)  # Database query executed here

# Use .update() with F() for bulk operations instead of looping
# Instead of:
for product in Product.objects.filter(category='electronics'):
    product.view_count += 1
    product.save()  # Inefficient: multiple queries

# Do:
Product.objects.filter(category='electronics').update(
    view_count=F('view_count') + 1  # Single query
)