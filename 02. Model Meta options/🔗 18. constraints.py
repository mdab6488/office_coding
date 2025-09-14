# Purpose: Defines database constraints (e.g., unique constraints, checks).

from django.db import models

class Volume(models.Model):
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    volume_number = models.CharField(max_length=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['journal', 'volume_number'],
                name='unique_journal_volume'
            ),
            models.CheckConstraint(
                check=models.Q(volume_number__gte='0'),
                name='volume_number_positive'
            )
        ]

# Note: UniqueConstraint is preferred over unique_together (which is legacy) 