# When working with deferred fields (fields that weren't loaded initially), you can customize how they're loaded:

class Article(models.Model):
    # ... fields as above ...
    
    def refresh_from_db(self, using=None, fields=None, **kwargs):
        # If any deferred field is being refreshed, load all deferred fields
        if fields is not None:
            deferred_fields = self.get_deferred_fields()
            # Check if any deferred field is in the fields to be refreshed
            if set(fields).intersection(deferred_fields):
                # Load all deferred fields
                fields = set(fields).union(deferred_fields)
        
        super().refresh_from_db(using, fields, **kwargs)

# When loading article with deferred content
article = Article.objects.defer('content').get(pk=1)
# Later refresh including content
article.refresh_from_db(fields=['title', 'content'])  # Will load all deferred fields