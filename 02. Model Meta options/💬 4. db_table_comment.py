# Purpose: Adds a comment to the database table for documentation.

class Answer(models.Model):
    content = models.TextField()

    class Meta:
        db_table_comment = "Stores answers to frequently asked questions"
