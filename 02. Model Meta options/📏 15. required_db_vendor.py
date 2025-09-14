# Purpose: Restricts the model to specific database vendors (e.g., 'postgresql', 'mysql').

class VendorModel(models.Model):
    data = models.JSONField()  # JSON field is well-supported in PostgreSQL

    class Meta:
        required_db_vendor = 'postgresql'

