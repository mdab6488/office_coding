# Objects can be deleted using the delete() method:

article = Article.objects.get(pk=1)
article.delete()  # Deletes the object from database

# Delete with custom behavior
class Article(models.Model):
    # ... fields as above ...
    
    def delete(self, *args, **kwargs):
        # Custom pre-delete logic
        self.archive_content()
        
        # Call the "real" delete() method
        super().delete(*args, **kwargs)
        
        # Custom post-delete logic
        self.update_related_objects()