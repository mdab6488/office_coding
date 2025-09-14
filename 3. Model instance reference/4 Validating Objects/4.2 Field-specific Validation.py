# Each field type in Django has built-in validation. You can also add custom validators to fields:

from django.core.validators import RegexValidator

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    email = models.EmailField()  # Has built-in email validation

# Example of field validation
customer = Customer(name="John Doe", phone="invalid", email="not-an-email")
try:
    customer.full_clean()
except ValidationError as e:
    print(e.message_dict)
    # Output: {
    #   'phone': ['Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.'],
    #   'email': ['Enter a valid email address.']
    # } 