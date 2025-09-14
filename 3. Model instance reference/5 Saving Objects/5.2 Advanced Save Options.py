# Save only specific fields to optimize performance
article.title = "New Title"
article.content = "Updated content"
article.save(update_fields=['title'])  # Only update title field

# Save to a specific database
article.save(using='replica_db')

# Control update vs insert behavior
article.save(force_insert=True)  # Force INSERT
article.save(force_update=True)  # Force UPDATE