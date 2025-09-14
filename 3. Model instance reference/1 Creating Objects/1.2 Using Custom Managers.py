# For more complex object creation logic, creating a custom manager is often the preferred approach. This keeps creation logic encapsulated and reusable.

class BookManager(models.Manager):
    def create_book(self, title, publication_date=None, isbn=None):
        """
        Creates and saves a Book with the given title and optional 
        publication date and ISBN.
        """
        book = self.model(
            title=title,
            publication_date=publication_date,
            isbn=isbn
        )
        # Add any additional pre-save logic here
        if isbn is None:
            book.isbn = self.generate_temp_isbn()
        book.save()
        return book
    
    def generate_temp_isbn(self):
        # Logic to generate temporary ISBN
        return "TEMP_ISBN_12345"

class Book(models.Model):
    # ... fields as above ...
    
    objects = BookManager()

# Usage
book = Book.objects.create_book("Advanced Django Patterns")