# Django provides multiple ways to create model instances, each with specific use cases and advantages.

# The most straightforward way to create a model instance is by directly instantiating the model class with keyword arguments corresponding to field names. Note that this doesn't save the object to the database - you must explicitly call save().

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)

# Create a book instance without saving to database
book = Book(title="Django for Beginners", publication_date="2023-01-15", isbn="9781234567890")
print(book.title)  # Output: Django for Beginners
print(book.id)     # Output: None (not saved yet)

# Save to database
book.save()
print(book.id)     # Output: 1 (or whatever ID was assigned)