# Complex conditional aggregation
from datetime import date
from django.db.models import Avg

current_year = date.today().year

# Average value by account type for recently registered clients
stats = Client.objects.aggregate(
    avg_gold_recent=Avg(
        'value',
        filter=Q(account_type=Client.GOLD, registered_on__year=current_year)
    ),
    avg_platinum_recent=Avg(
        'value', 
        filter=Q(account_type=Client.PLATINUM, registered_on__year=current_year)
    ),
    avg_other=Avg(
        'value',
        filter=~Q(account_type__in=[Client.GOLD, Client.PLATINUM])
    )
)

# Conditional aggregation with the filter argument provides a clean and efficient way to calculate multiple aggregates in a single query .

