# Conditional expressions that return boolean values can be used directly in filters, enabling complex filtering logic.

from datetime import date, timedelta

# Find gold clients registered more than a month ago and platinum clients registered more than a year ago
a_month_ago = date.today() - timedelta(days=30)
a_year_ago = date.today() - timedelta(days=365)

clients = Client.objects.filter(
    registered_on__lte=Case(
        When(account_type=Client.GOLD, then=a_month_ago),
        When(account_type=Client.PLATINUM, then=a_year_ago),
    ),
).values_list("name", "account_type")

# Example output: [('Jack Black', 'P')]


# This approach allows you to apply different filtering criteria to different subsets of your data in a single query 