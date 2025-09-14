# Purpose: Defines database indexes for the model to improve query performance.

from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['email'], name='unique_email_idx'),
        ]
        
# Note: Use models.Index for single or composite indexes .

