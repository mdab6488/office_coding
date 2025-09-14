# Django supports three types of model inheritance: abstract base classes, multi-table inheritance, and proxy models.

# Abstract base classes are useful when you want to share common fields and methods across multiple models without creating a separate database table for the base class.

from django.db import models

class TimeStampedModel(models.Model):
    """Abstract base class with timestamp fields"""
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  # This model won't create a database table

class AuditModel(models.Model):
    """Abstract base class with audit fields"""
    created_by = models.ForeignKey(
        'auth.User', 
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_created'
    )
    modified_by = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_modified'
    )
    
    class Meta:
        abstract = True

# Concrete models that inherit from abstract base classes
class Article(TimeStampedModel, AuditModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Comment(TimeStampedModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return f"Comment by {self.author} on {self.article}"

# Example usage
article = Article.objects.create(
    title="Django Models Guide",
    content="Comprehensive guide to Django models...",
    created_by=User.objects.first(),
    modified_by=User.objects.first()
)
print(article.created)  # Automatically set when created
print(article.modified)  # Automatically updated when saved