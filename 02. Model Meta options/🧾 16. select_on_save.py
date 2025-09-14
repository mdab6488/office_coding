# Purpose: Enables old-style get() query before saving to determine if INSERT or UPDATE should be used. Not recommended for new code.

class LegacyModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        select_on_save = True  # Mimics pre-Django 1.5 behavior

