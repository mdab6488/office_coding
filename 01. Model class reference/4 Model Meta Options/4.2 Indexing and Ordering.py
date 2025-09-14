from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    loyalty_points = models.PositiveIntegerField(default=0)
    
    class Meta:
        # Composite indexing for better query performance
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['date_joined'], name='joined_date_idx'),
        ]
        
        # Ordering by multiple fields
        ordering = ['last_name', 'first_name']
        
        # Get the latest by date_joined
        get_latest_by = 'date_joined'

# Example usage
latest_customer = Customer.objects.latest()  # Gets the most recently joined customer
customers_a_to_z = Customer.objects.all()  # Ordered by last_name, then first_name

# Table: Common Meta Options and Their Purposes
"""
Meta Option	Description	Example
ordering	Default ordering for queries	ordering = ['-created', 'name']
verbose_name	Human-readable name for a single object	verbose_name = 'Product'
verbose_name_plural	Human-readable name for multiple objects	verbose_name_plural = 'Products'
db_table	Custom database table name	db_table = 'custom_product_table'
abstract	Whether the model is abstract	abstract = True
unique_together	Unique constraints for multiple fields	unique_together = [['field1', 'field2']]
indexes	Database indexes for better performance	indexes = [models.Index(fields=['field1', 'field2'])]
"""
