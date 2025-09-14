# Using conditional expressions with database functions
from django.db.models.functions import Concat

clients = Client.objects.annotate(
    status_description=Case(
        When(account_type=Client.GOLD, then=Concat(Value('Gold Member: '), F('name'))),
        When(account_type=Client.PLATINUM, then=Concat(Value('Platinum Member: '), F('name'))),
        default=Concat(Value('Member: '), F('name'))),
    )
)

# Conditional expressions can be combined with database functions like Concat to create powerful dynamic values directly in your queries 