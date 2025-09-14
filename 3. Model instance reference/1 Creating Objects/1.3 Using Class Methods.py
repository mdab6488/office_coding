# You can also add class methods to your model for custom creation logic, though this is less common than using custom managers.

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    
    @classmethod
    def create_with_default_date(cls, title, isbn=None):
        """
        Creates a book with the current date as publication date
        """
        import datetime
        return cls.objects.create(
            title=title,
            publication_date=datetime.date.today(),
            isbn=isbn
        )

# Usage
book = Book.create_with_default_date("Django Patterns")