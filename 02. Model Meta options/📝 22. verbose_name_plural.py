# Purpose: Human-readable plural name for the model.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"  # Avoids default "Categorys"

"""📋 Summary of Key Recommendations"""
# Use constraints with UniqueConstraint instead of unique_together.
# Use indexes with models.Index instead of index_together.
# proxy = True is useful for creating proxy models that inherit behavior.
# managed = False is essential for working with existing database tables.
# Always set ordering for predictable query results.
# Use permissions to add custom permissions beyond the defaults.
