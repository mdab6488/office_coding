# Purpose: Specifies the default field to use for latest() and earliest() methods.

class Event(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField()

    class Meta:
        get_latest_by = ['-priority', 'timestamp']  # Latest by priority descending, then timestamp ascending

