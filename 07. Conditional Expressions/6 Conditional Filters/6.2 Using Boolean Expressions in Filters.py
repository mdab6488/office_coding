# Using boolean expressions with Exists in filters
non_unique_account_type = (
    Client.objects.filter(
        account_type=OuterRef("account_type"),
    )
    .exclude(pk=OuterRef("pk"))
    .values("pk")
)

# Filter clients with unique account types
clients_with_unique_types = Client.objects.filter(~Exists(non_unique_account_type))

# This example demonstrates how to use complex boolean logic with subqueries to filter records based on conditions that require checking related data .

