# Verifying custom lookups is crucial to ensure they work as expected:

from django.test import TestCase
from myapp.models import Product

class CustomLookupTests(TestCase):
    
    def test_not_equal_lookup(self):
        # Create test data
        Product.objects.create(name="Laptop", price=1000)
        Product.objects.create(name="Phone", price=500)
        
        # Test not equal lookup
        results = Product.objects.filter(name__ne="Laptop")
        self.assertEqual(results.count(), 1)
        self.assertEqual(results.first().name, "Phone")
    
    def test_absolute_value_lookup(self):
        # Create test data with positive and negative values
        Experiment.objects.create(change=25)
        Experiment.objects.create(change=-30)
        Experiment.objects.create(change=15)
        
        # Test absolute value lookup
        results = Experiment.objects.filter(change__abs__lt=27)
        self.assertEqual(results.count(), 2)  # Should match 25 and 15
        
# Comprehensive testing ensures your custom lookups work correctly with different data scenarios and database backends.

