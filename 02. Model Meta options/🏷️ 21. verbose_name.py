# Purpose: Human-readable name for the model (singular).

class Customer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "client"

