# Purpose: Sets the default ordering for queries.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', 'name']  # Newest first, then by name ascending

# Note: Use ? for random ordering: ordering = ['?'] (caution: performance impact) .

