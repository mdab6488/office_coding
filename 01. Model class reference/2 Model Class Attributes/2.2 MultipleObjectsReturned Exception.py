# The MultipleObjectsReturned exception occurs when a query that should return a single object unexpectedly finds multiple matches. This is particularly useful when using the get() method with fields that aren't guaranteed to be unique.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)  # Should be unique
    price = models.DecimalField(max_digits=10, decimal_places=2)

# Example usage
try:
    product = Product.objects.get(name="Generic Product")  # Might have duplicates
except Product.MultipleObjectsReturned:
    print("Multiple products found with the same name!")
    # Handle the error appropriately, perhaps using filter() instead
    products = Product.objects.filter(name="Generic Product")
    product = products.first()  # Get the first match