# The output_field parameter specifies the type of field that should be returned by an expression. This is necessary when Django cannot automatically determine the result type of complex expressions .

from django.db.models import DateTimeField, ExpressionWrapper, F, DurationField
from django.db.models.functions import Now

# Without output_field, Django doesn't know the field type for expression
expires = ExpressionWrapper(
    F('active_at') + F('duration'), 
    output_field=DateTimeField()
)

Ticket.objects.annotate(expires=expires)

# Different field types require explicit output_field
Product.objects.annotate(
    price_difference=F('price') - F('cost_price'),
    # output_field not strictly needed here as Django can infer numeric type
)

# When mixing types, output_field is essential
Company.objects.annotate(
    employee_ratio=F('num_employees') / F('num_chairs'),
    # output_field=FloatField() would be appropriate here
)