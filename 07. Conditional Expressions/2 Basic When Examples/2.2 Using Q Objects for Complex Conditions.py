# Complex conditions using Q objects
When(Q(name__startswith="John") | Q(name__startswith="Paul"), then="name")

# Combining multiple conditions with Q objects
When(Q(account_type=Client.GOLD) & Q(registered_on__year=2023), then="special_gold")    

# Q objects enable you to create complex query conditions with OR (|), AND (&), and NOT (~) operators, providing flexibility for sophisticated conditional logic 