# Django models come with several built-in methods that you can override to customize model behavior. The most commonly overridden methods include __str__(), save(), and delete().

from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Custom save logic: generate slug from name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        
        # Ensure slug is unique
        original_slug = self.slug
        counter = 1
        while Category.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1
            
        super().save(*args, **kwargs)  # Call the "real" save() method
    
    def delete(self, *args, **kwargs):
        # Custom delete logic: perform cleanup before deletion
        print(f"Deleting category: {self.name}")
        # Additional cleanup operations could go here
        super().delete(*args, **kwargs)  # Call the "real" delete() method

# Example usage
category = Category(name="Web Development")
category.save()  # Automatically generates slug "web-development"
print(category)  # Output: "Web Development" (uses __str__ method)
category.delete()  # Output: "Deleting category: Web Development"