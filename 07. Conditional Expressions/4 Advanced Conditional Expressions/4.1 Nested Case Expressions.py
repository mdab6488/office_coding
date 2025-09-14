# For more complex scenarios, conditional expressions can be combined, nested, and used with other Django query expressions.

# Nested Case example for complex categorization
clients = Client.objects.annotate(
    status=Case(
        When(account_type=Client.PLATINUM, then=Value("Premium")),
        When(account_type=Client.GOLD, 
             then=Case(
                 When(registered_on__year=date.today().year, then=Value("New Gold")),
                 default=Value("Existing Gold"),
             )),
        default=Value("Standard"),
    )
)

#Nested Case expressions allow you to create multi-level conditional logic for handling complex business rules directly in your database queries 