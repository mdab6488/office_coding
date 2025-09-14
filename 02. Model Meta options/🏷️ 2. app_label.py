# Purpose: Specifies the app a model belongs to if it’s defined outside an app in INSTALLED_APPS.

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'myapp'  # Even if model is in a different module

# Use Case: Useful for reusable apps or when organizing code into modules 