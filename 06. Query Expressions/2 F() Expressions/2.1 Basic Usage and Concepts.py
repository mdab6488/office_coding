# The F() expression represents the value of a model field or annotated column, allowing database-level operations without retrieving values into Python memory. Django uses F() objects to generate SQL expressions that describe required operations at the database level .

from django.db.models import F

# Incrementing a field value without F()
product = Product.objects.get(id=1)
product.quantity += 10
product.save()  # Requires two database operations

# Using F() for the same operation
Product.objects.filter(id=1).update(quantity=F('quantity') + 10)  # Single database operation