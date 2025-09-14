# The save() method is used to persist model instances to the database. Django provides various options to control the save behavior.

# Create a new object
article = Article(title="New Article", content="Content")
article.save()  # Performs INSERT

# Update an existing object
article.title = "Updated Title"
article.save()  # Performs UPDATE

# Save with custom options
article.save(force_insert=True)  # Force INSERT even if object exists