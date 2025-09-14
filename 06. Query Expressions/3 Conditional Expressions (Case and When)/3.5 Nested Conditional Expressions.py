# For more complex logic, you can nest conditional expressions to handle multiple scenarios .

# Nested conditional logic
products = Product.objects.annotate(
    pricing_tier=Case(
        When(discontinued=True, then=Value('discontinued')),
        When(
            Q(price__lt=50) & Q(stock__lt=10),
            then=Case(
                When(price__lt=10, then=Value('low_cost_limited')),
                When(price__lt=50, then=Value('mid_cost_limited')),
                output_field=CharField()
            )
        ),
        When(price__lt=10, then=Value('low_cost')),
        When(price__lt=50, then=Value('mid_cost')),
        default=Value('premium'),
        output_field=CharField()
    )
)   