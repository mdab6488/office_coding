# Django allows you to customize how model instances are loaded from the database by overriding the from_db() class method. This is useful for tracking initial field values or implementing special loading logic.

from django.db.models import DEFERRED

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    
    @classmethod
    def from_db(cls, db, field_names, values):
        """
        Custom from_db implementation to store initial values
        """
        # Default implementation (subject to change)
        if len(values) != len(cls._meta.concrete_fields):
            values = list(values)
            values.reverse()
            values = [
                values.pop() if f.attname in field_names else DEFERRED
                for f in cls._meta.concrete_fields
            ]
        instance = cls(*values)
        instance._state.adding = False
        instance._state.db = db
        
        # Store original field values
        instance._loaded_values = dict(
            zip(field_names, (value for value in values if value is not DEFERRED))
        )
        return instance
    
    def save(self, *args, **kwargs):
        # Check if author has changed
        if not self._state.adding and hasattr(self, '_loaded_values'):
            if self.author_id != self._loaded_values.get('author_id'):
                raise ValueError("Changing author is not allowed")
        super().save(*args, **kwargs)

# When loading an article from database, it will have _loaded_values
article = Article.objects.get(pk=1)
print(article._loaded_values)  # Output: {'title': 'Original', 'content': '...', ...}