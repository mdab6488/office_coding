# Django allows you to defer loading of specific fields for performance optimization:

# Load article without the content field (which could be large)
article = Article.objects.defer('content').get(pk=1)
print(article.title)     # This is available
# print(article.content) # This would trigger additional database query

# Check which fields are deferred
print(article.get_deferred_fields())  # Output: {'content'}

# Load deferred fields when needed
article.refresh_from_db(fields=['content'])
print(article.get_deferred_fields())  # Output: set() (no deferred fields)