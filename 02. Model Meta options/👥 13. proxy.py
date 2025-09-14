# Purpose: If True, the model is a proxy model (inherits from another model without creating a new database table).

class Person(models.Model):
    name = models.CharField(max_length=100)

class OrderedPerson(Person):
    class Meta:
        proxy = True
        ordering = ['name']  # Adds ordering without affecting Person

