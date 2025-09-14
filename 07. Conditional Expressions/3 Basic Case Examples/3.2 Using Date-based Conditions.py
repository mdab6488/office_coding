# Annotate clients with discounts based on registration date
a_month_ago = date.today() - timedelta(days=30)
a_year_ago = date.today() - timedelta(days=365)

clients = Client.objects.annotate(
    discount=Case(
        When(registered_on__lte=a_year_ago, then=Value("10%")),
        When(registered_on__lte=a_month_ago, then=Value("5%")),
        default=Value("0%"),
    )
).values_list("name", "discount")

# Example output: [('Jane Doe', '5%'), ('James Smith', '0%'), ('Jack Black', '10%')]

# When using Case with multiple conditions, remember that conditions are evaluated in order, and the first matching condition determines the result 