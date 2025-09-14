# You can override the save() method to add custom behavior before or after saving:

class Article(models.Model):
    # ... fields as above ...
    
    def save(self, *args, **kwargs):
        # Custom pre-save logic
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        
        # Check if specific fields have changed
        if self.pk:
            original = Article.objects.get(pk=self.pk)
            if original.title != self.title:
                print("Title has changed!")
        
        # Call the "real" save() method
        super().save(*args, **kwargs)
        
        # Custom post-save logic
        self.update_search_index()
    
    def update_search_index(self):
        # Update search index after save
        pass

# Usage
article = Article(title="My New Article", content="Content")
article.save()  # Will automatically generate slug
print(article.slug)  # Output: "my-new-article"