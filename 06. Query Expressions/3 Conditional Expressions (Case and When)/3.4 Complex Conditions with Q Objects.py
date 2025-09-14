# You can combine Case/When expressions with Q objects to create complex conditional logic 

from django.db.models import Q

# Complex conditional annotation using Q objects
clients = Client.objects.annotate(
    priority_status=Case(
        When(
            Q(account_type=Client.PLATINUM) | 
            Q(registered_on__lte=a_year_ago, account_type=Client.GOLD),
            then=Value('high_priority')
        ),
        When(
            Q(account_type=Client.GOLD) |
            Q(registered_on__lte=a_year_ago, account_type=Client.REGULAR),
            then=Value('medium_priority')
        ),
        default=Value('standard_priority'),
        output_field=CharField()
    )
)