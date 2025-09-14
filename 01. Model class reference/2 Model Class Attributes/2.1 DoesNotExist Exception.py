# The DoesNotExist exception is a special exception that Django raises when a query doesn't find any matching object. This exception is specific to each model class, allowing you to catch exceptions for particular models.

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

# Example usage with exception handling
try:
    article = Article.objects.get(id=999)  # Non-existent ID
except Article.DoesNotExist:
    print("Article not found. Creating a new one...")
    article = Article(title="Default Title", content="Default content")
    article.save()