# You can use conditional expressions directly in filters for complex filtering logic .

from datetime import date, timedelta
from django.db.models import Case, When, Value, DateField

a_month_ago = date.today() - timedelta(days=30)
a_year_ago = date.today() - timedelta(days=365)

# Filter using Case/When expressions
Client.objects.filter(
    registered_on__lte=Case(
        When(account_type=Client.GOLD, then=a_month_ago),
        When(account_type=Client.PLATINUM, then=a_year_ago),
    )
)

# Boolean conditions in filters
from django.db.models import Exists, OuterRef
high_value_clients = Client.objects.filter(
    Exists(
        Order.objects.filter(
            client=OuterRef('pk'),
            total__gt=1000
        )
    )
)