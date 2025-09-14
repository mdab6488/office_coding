# Inefficient approach (multiple queries)
above_3yrs = date.today() - timedelta(days=365 * 3)
above_2yrs = date.today() - timedelta(days=365 * 2)

Employee.objects.filter(joined_on__lt=above_3yrs).update(account_type="PLATINUM")
Employee.objects.filter(joined_on__lt=above_2yrs).update(account_type="GOLD")

# Efficient approach (single query)
Employee.objects.update(
    account_type=Case(
        When(joined_on__lte=above_3yrs, then=Value("PLATINUM")),
        When(joined_on__lte=above_2yrs, then=Value("GOLD")),
        default=Value("REGULAR")
    ),
)

# Using conditional expressions for bulk updates can dramatically reduce database queries, improving application performance and reducing database load 