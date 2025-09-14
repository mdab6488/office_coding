from django.db.models import IntegerField, Sum

# Count clients by account type using Case expressions
counts = Client.objects.aggregate(
    regular=Sum(
        Case(When(account_type=Client.REGULAR, then=1),
             output_field=IntegerField(),
             default=0)
    ),
    gold=Sum(
        Case(When(account_type=Client.GOLD, then=1),
             output_field=IntegerField(),
             default=0)
    ),
    platinum=Sum(
        Case(When(account_type=Client.PLATINUM, then=1),
             output_field=IntegerField(),
             default=0)
    )
)

# This approach is useful on databases that don't support the FILTER clause, as it emulates the functionality using CASE statements 