# The objects attribute is the default manager for every Django model, providing the interface for database query operations. You can customize the default manager or add additional managers to your models.

from django.db import models
from django.utils import timezone

class PublishedManager(models.Manager):
    """Custom manager for published posts"""
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_date = models.DateTimeField(default=timezone.now)
    
    # Default manager
    objects = models.Manager()
    
    # Custom manager
    published = PublishedManager()
    
    def __str__(self):
        return self.title

# Example usage
all_posts = Post.objects.all()  # All posts including drafts
published_posts = Post.published.all()  # Only published posts
recent_published = Post.published.filter(published_date__gte=timezone.now() - timezone.timedelta(days=7))