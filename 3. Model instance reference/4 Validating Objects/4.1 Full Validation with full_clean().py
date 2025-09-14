4.3 Partial Validation with exclude
# Django provides a comprehensive validation system for models that operates at multiple levels.

# The full_clean() method performs complete validation, including field validation, model-level validation, and uniqueness constraints.

from django.core.exceptions import ValidationError
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices=[
        ('draft', 'Draft'),
        ('published', 'Published'),
    ])
    pub_date = models.DateField(null=True, blank=True)
    content = models.TextField()
    
    def clean(self):
        """
        Model-level validation
        """
        # Don't allow draft entries to have a publication date
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError({
                'pub_date': 'Draft entries may not have a publication date.'
            })
        
        # Set publication date for published items if not set
        if self.status == 'published' and self.pub_date is None:
            from datetime import date
            self.pub_date = date.today()
    
    def validate_unique(self, exclude=None):
        """
        Custom uniqueness validation
        """
        super().validate_unique(exclude)
        
        # Add custom uniqueness checks
        if Article.objects.filter(
            slug__iexact=self.slug  # Case-insensitive check
        ).exclude(pk=self.pk).exists():
            raise ValidationError({
                'slug': 'Article with this Slug already exists (case-insensitive).'
            })

# Validation examples
article = Article(
    title="My Article",
    slug="my-article",
    status="draft",
    pub_date="2023-01-01",  # This should cause validation error
    content="Lorem ipsum..."
)

try:
    article.full_clean()  # This will raise ValidationError
except ValidationError as e:
    print(e.message_dict)
    # Output: {'pub_date': ['Draft entries may not have a publication date.']}

# Test uniqueness validation
article2 = Article(
    title="Another Article",
    slug="MY-ARTICLE",  # Same slug but different case
    status="published",
    content="More content..."
)

try:
    article2.full_clean()  # This will raise ValidationError due to case-insensitive check
except ValidationError as e:
    print(e.message_dict)
    # Output: {'slug': ['Article with this Slug already exists (case-insensitive).']}