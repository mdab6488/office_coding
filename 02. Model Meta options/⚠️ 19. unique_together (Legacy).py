# Purpose: Ensures uniqueness of sets of fields (use UniqueConstraint in new code).

class Volume(models.Model):
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    volume_number = models.CharField(max_length=10)

    class Meta:
        unique_together = [['journal', 'volume_number']]  # Legacy approach

# Deprecation Note: Prefer constraints with UniqueConstraint 