# The When class is used to define individual conditions within conditional expressions. It can be used with various types of conditions, including field lookups, Q objects, and boolean expressions.

from django.db.models import F, Q, When
from datetime import date

# Basic field comparison
When(account_type=Client.GOLD, then="name")

# Using field lookups in conditions
When(
    registered_on__gt=date(2014, 1, 1),
    registered_on__lt=date(2015, 1, 1),
    then="account_type",
)

# Using F expressions in conditions
When(account_type=Client.GOLD, then=F("name"))

# Field lookups in When expressions follow the same pattern as filter() lookups, allowing you to use the same syntax you're already familiar with from filtering querysets .

