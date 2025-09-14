# Update multiple fields conditionally
Client.objects.update(
    account_type=Case(
        When(registered_on__lte=a_year_ago, then=Value(Client.PLATINUM)),
        When(registered_on__lte=a_month_ago, then=Value(Client.GOLD)),
        default=Value(Client.REGULAR),
    ),
    status=Case(
        When(registered_on__lte=a_year_ago, then=Value('legacy')),
        When(registered_on__lte=a_month_ago, then=Value('recent')),
        default=Value('new')),
    )
)

# While Django's ORM doesn't natively support updating multiple fields with different conditions in a single call, you can execute multiple update statements in a transaction for atomic updates 