# Purpose: Specifies the database tablespace for the table (if supported by the database).

class Report(models.Model):
    data = models.JSONField()

    class Meta:
        db_tablespace = 'reports_tablespace'
