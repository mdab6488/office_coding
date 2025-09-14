# Purpose: Defines composite indexes (use indexes with models.Index in new code).

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    class Meta:
        index_together = [
            ['user', 'timestamp'],  # Legacy composite index
        ]
        
# Deprecation Note: Prefer indexes option 