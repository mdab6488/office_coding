# You can use Case and When expressions to perform conditional updates based on specific criteria 
from datetime import date, timedelta

a_month_ago = date.today() - timedelta(days=30)
a_year_ago = date.today() - timedelta(days=365)

# Update account_type based on registration date
Client.objects.update(
    account_type=Case(
        When(registered_on__lte=a_year_ago, then=Value(Client.PLATINUM)),
        When(registered_on__lte=a_month_ago, then=Value(Client.GOLD)),
        default=Value(Client.REGULAR),
        output_field=CharField()
    )
)