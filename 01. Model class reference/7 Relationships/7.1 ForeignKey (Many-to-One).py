# A ForeignKey represents a many-to-one relationship, where multiple instances of one model are related to a single instance of another model.

from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    website = models.URLField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # ManyToManyField for genres
    genres = models.ManyToManyField('Genre', related_name='books')
    
    def __str__(self):
        return self.title
    
    def author_name(self):
        return str(self.author)

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

# Example usage
author = Author.objects.get(pk=1)
publisher = Publisher.objects.get(pk=1)

# Create a new book
book = Book.objects.create(
    title="Advanced Django Patterns",
    author=author,
    publisher=publisher,
    isbn="9781234567897",
    publication_date="2023-06-15",
    price=49.99
)

# Add genres to the book
fiction = Genre.objects.get(name="Fiction")
tech = Genre.objects.get(name="Technology")
book.genres.add(fiction, tech)

# Query related objects
author_books = author.books.all()  # All books by this author
publisher_books = publisher.book_set.all()  # All books from this publisher
genre_books = fiction.books.all()  # All books in this genre