# When expressions involve different field types, you must use output_field to ensure Django handles the result correctly .

from django.db.models import FloatField, DecimalField, IntegerField

# Mixing DecimalField and FloatField requires explicit output_field
Product.objects.annotate(
    discounted_price=ExpressionWrapper(
        F('price') * (1 - F('discount_percentage') / 100),
        output_field=FloatField()
    )
)

# Arithmetic between different numeric types
Company.objects.annotate(
    chairs_per_employee=ExpressionWrapper(
        F('num_chairs') / F('num_employees'),
        output_field=FloatField()
    )
)

# Date arithmetic
from django.db.models import DurationField
Event.objects.annotate(
    duration=ExpressionWrapper(
        F('end_time') - F('start_time'),
        output_field=DurationField()
    )
)