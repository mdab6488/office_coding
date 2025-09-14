# For more control over the refresh process, you can override the refresh_from_db method:

class Article(models.Model):
    # ... fields as above ...
    
    def refresh_from_db(self, using=None, fields=None, **kwargs):
        # Custom logic before refresh
        print(f"Refreshing article {self.pk}")
        
        # Call parent implementation
        super().refresh_from_db(using, fields, **kwargs)
        
        # Custom logic after refresh
        self._cached_related = None  # Clear related cache

# Usage
article.refresh_from_db()