# Combine conditional expressions with arithmetic operations
from django.db.models import ExpressionWrapper, FloatField

# Calculate discounted price based on account type
clients = Client.objects.annotate(
    discounted_value=Case(
        When(account_type=Client.GOLD, then=ExpressionWrapper(F('value') * 0.95, output_field=FloatField())),
        When(account_type=Client.PLATINUM, then=ExpressionWrapper(F('value') * 0.90, output_field=FloatField())),
        default=F('value'),
        output_field=FloatField()
    )
)

# When combining different field types in expressions, you may need to use ExpressionWrapper to explicitly specify the output_field 