# Combine conditional expressions with Q objects for complex filtering
from django.db.models import Value

clients = Client.objects.filter(
    Q(account_type=Client.REGULAR) |
    Q(
        registered_on__lte=Case(
            When(account_type=Client.GOLD, then=Value(a_month_ago)),
            When(account_type=Client.PLATINUM, then=Value(a_year_ago)),
        )
    )
)

# Combining Q objects with conditional expressions provides maximum flexibility for building complex query conditions 