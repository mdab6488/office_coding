# Django automatically determines whether to INSERT or UPDATE based on the object's primary key:

# Create new object (no primary key)
article = Article(title="New Article")
article.save()  # INSERT (creates new record)

# Update existing object (has primary key)
article.title = "Updated Title"
article.save()  # UPDATE (updates existing record)

# Force specific behavior
article.save(force_insert=True)  # Force INSERT (may cause error if pk exists)
article.save(force_update=True)  # Force UPDATE (may cause error if pk doesn't exist)