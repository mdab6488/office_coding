from django.db.models import Count, Q

# Count clients by account type using filter argument
counts = Client.objects.aggregate(
    regular=Count("pk", filter=Q(account_type=Client.REGULAR)),
    gold=Count("pk", filter=Q(account_type=Client.GOLD)),
    platinum=Count("pk", filter=Q(account_type=Client.PLATINUM)),
)

# Result: {'regular': 2, 'gold': 1, 'platinum': 3}

# This approach uses SQL's FILTER WHERE syntax where supported, which can provide better performance than equivalent CASE statements 