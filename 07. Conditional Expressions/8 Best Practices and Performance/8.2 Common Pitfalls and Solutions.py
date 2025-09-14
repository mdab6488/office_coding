# Field Type Conflicts: When combining different field types, explicitly specify output_field to avoid errors.

# Explicit output_field to avoid type conflicts
from django.db.models import DateTimeField, ExpressionWrapper

Ticket.objects.annotate(
    expires=ExpressionWrapper(
        F("active_at") + F("duration"), 
        output_field=DateTimeField()
    )
)

# Then Keyword Conflict: If a model has a field named then, use alternative syntax to avoid conflicts.

# Handling field name conflicts with 'then'
When(then__exact=0, then=1)
# or
When(Q(then=0), then=1) 

# Condition Evaluation Order: Conditions are evaluated in order, so place more specific conditions before general ones.
# Correct evaluation order
Case(
    When(price__gte=50, then=Value('expensive')),  # More specific condition
    When(price__gte=10, then=Value('moderate')),   # General condition
    default=Value('cheap')
)
