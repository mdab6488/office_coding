# The Case expression evaluates a series of When conditions in order and returns the matching result expression. It works similarly to Python's if...elif...else statements 

from django.db.models import Case, Value, When
from datetime import date, timedelta

# Annotate clients with discounts based on account type
clients = Client.objects.annotate(
    discount=Case(
        When(account_type=Client.GOLD, then=Value("5%")),
        When(account_type=Client.PLATINUM, then=Value("10%")),
        default=Value("0%"),
    )
).values_list("name", "discount")

# Example output: [('Jane Doe', '0%'), ('James Smith', '5%'), ('Jack Black', '10%')]\\@ 

# This example demonstrates how to annotate querysets with computed values based on specific conditions, similar to a SQL CASE statement 