# Purpose: Overrides the default database table name (which is appname_modelname).

class Book(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'library_books'  # Table will be named "library_books"
        
# Note: For Oracle, use quoted names to avoid case issues: db_table = '"book_table"' 