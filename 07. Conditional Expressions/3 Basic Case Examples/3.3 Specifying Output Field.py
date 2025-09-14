from django.db.models import BooleanField

# Annotate products with stock status
from .models import Product

products = Product.objects.annotate(
    in_stock=Case(
        When(quantity__gt=0, then=Value(True)),
        default=Value(False),
        output_field=BooleanField()
    )
)

# It's important to specify the output_field when Django cannot automatically determine the result type, particularly when mixing different field types or when using boolean values .

