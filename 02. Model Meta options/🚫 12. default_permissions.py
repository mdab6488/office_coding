# Purpose: Customizes the default permissions (add, change, delete, view).

class ReadOnlyModel(models.Model):
    data = models.TextField()

    class Meta:
        default_permissions = ()  # No default permissions

