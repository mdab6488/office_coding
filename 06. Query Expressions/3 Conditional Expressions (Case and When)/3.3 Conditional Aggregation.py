# Conditional aggregation allows you to perform counts or other aggregates based on specific conditions .

from django.db.models import Count, Q

# Get counts for each account type using conditional aggregation
account_stats = Client.objects.aggregate(
    regular=Count('pk', filter=Q(account_type=Client.REGULAR)),
    gold=Count('pk', filter=Q(account_type=Client.GOLD)),
    platinum=Count('pk', filter=Q(account_type=Client.PLATINUM)),
)

# This generates SQL with FILTER WHERE or CASE statements depending on database