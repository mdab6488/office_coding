# Django model instances have several other useful methods and properties.

# The pk property is an alias for the primary key, regardless of what the actual primary key field is named.

# Assuming Article has an AutoField primary key
article = Article.objects.get(title="Some Article")
print(article.pk)    # Same as article.id
print(article.id)    # The actual primary key value

# Even with custom primary key
class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    title = models.CharField(max_length=100)

book = Book(isbn="9781234567890", title="Django Book")
print(book.pk)       # Output: 9781234567890 (same as book.isbn)