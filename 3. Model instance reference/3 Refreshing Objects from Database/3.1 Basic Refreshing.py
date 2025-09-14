# Django provides the refresh_from_db() method to reload an object's values from the database, which is useful when you suspect the object's data might be stale.

# Create and retrieve an article
article = Article.objects.create(title="Original Title")
print(article.title)  # Output: Original Title

# Update the article directly in database (bypassing the object)
Article.objects.filter(pk=article.pk).update(title="Updated Title")

# The object still has the old value
print(article.title)  # Output: Original Title

# Refresh from database
article.refresh_from_db()
print(article.title)  # Output: Updated Title