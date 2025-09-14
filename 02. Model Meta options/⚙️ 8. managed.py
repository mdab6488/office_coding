# Purpose: If False, Django won’t create, modify, or delete the database table for this model.

class LegacyTable(models.Model):
    legacy_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False  # Table already exists in the database
        
# Use Case: For existing database tables or views 