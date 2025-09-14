# One of the key advantages of F() expressions is their ability to prevent race conditions by performing operations at the database level rather than in Python 

# Without F() - vulnerable to race conditions
product = Product.objects.get(id=1)
product.quantity -= 1  # If another process updates quantity here, we lose that update
product.save()

# With F() - atomic operation at database level
Product.objects.filter(id=1).update(quantity=F('quantity') - 1)

# Atomic increment for multiple records
Product.objects.filter(category='electronics').update(
    view_count=F('view_count') + 1
)