# Conditional expressions are particularly useful for performing bulk updates based on complex conditions, reducing the number of database queries needed.

from datetime import date, timedelta

# Update account_type based on registration date
a_month_ago = date.today() - timedelta(days=30)
a_year_ago = date.today() - timedelta(days=365)

Client.objects.update(
    account_type=Case(
        When(registered_on__lte=a_year_ago, then=Value(Client.PLATINUM)),
        When(registered_on__lte=a_month_ago, then=Value(Client.GOLD)),
        default=Value(Client.REGULAR),
    ),
)

# Verify the updates
Client.objects.values_list("name", "account_type")
# Example output: [('Jane Doe', 'G'), ('James Smith', 'R'), ('Jack Black', 'P')]

# Bulk updates with conditional expressions are significantly more efficient than updating individual records in a loop, especially for large datasets .

