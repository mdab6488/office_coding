# Django provides a wide variety of field types to represent different types of data in your models.

from django.db import models
import uuid

class Product(models.Model):
    # Basic fields
    name = models.CharField(max_length=200, help_text="Enter the product name")
    description = models.TextField(blank=True, help_text="Enter a detailed description")
    sku = models.SlugField(max_length=50, unique=True, help_text="Unique product identifier")
    
    # Numeric fields
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    rating = models.FloatField(null=True, blank=True)
    
    # Date and time fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    release_date = models.DateField(null=True, blank=True)
    
    # Boolean field
    active = models.BooleanField(default=True)
    
    # Choice field
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('home', 'Home & Garden'),
        ('books', 'Books & Media'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    
    # File fields
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    manual = models.FileField(upload_to='manuals/', null=True, blank=True)
    
    # UUID field
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # URL field
    product_url = models.URLField(blank=True, help_text="URL to product page")
    
    # Email field
    support_email = models.EmailField(blank=True, default="support@example.com")
    
    # JSON field (for storing structured data)
    specifications = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return self.name
    
    def profit_margin(self):
        """Calculate profit margin if cost is available"""
        if self.cost and self.price:
            return ((self.price - self.cost) / self.price) * 100
        return None

# Example usage
product = Product.objects.create(
    name="Wireless Headphones",
    description="High-quality wireless headphones with noise cancellation",
    sku="wh-1000xm4",
    price=349.99,
    cost=210.00,
    quantity=50,
    category="electronics",
    support_email="audio-support@example.com"
)

print(f"Profit margin: {product.profit_margin():.2f}%")  # Output: Profit margin: 40.00%