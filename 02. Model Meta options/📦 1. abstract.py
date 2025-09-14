# Purpose: Defines whether the model is an abstract base class. Abstract models are not created as database tables but serve as base classes for other models.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(BaseModel):
    name = models.CharField(max_length=100)

# Note: Customer inherits fields from BaseModel but BaseModel won't have its own database table 