# Purpose: Adds extra permissions to the model beyond the default add, change, delete, and view permissions.

class Task(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_close_task", "Can close task"),
            ("can_archive_task", "Can archive task"),
        ]

