from django.db.models import Exists, OuterRef

# Using boolean expressions with Exists
non_unique_account_type = (
    Client.objects.filter(
        account_type=OuterRef("account_type"),
    )
    .exclude(pk=OuterRef("pk"))
    .values("pk")
)
When(Exists(non_unique_account_type), then=Value("non unique"))

# Using lookup expressions
from django.db.models.lookups import GreaterThan, LessThan
When(
    GreaterThan(F("registered_on"), date(2014, 1, 1)) &
    LessThan(F("registered_on"), date(2015, 1, 1)),
    then="account_type",
)

# Boolean expressions and lookup expressions provide advanced conditional capabilities for scenarios where simple field lookups or Q objects are insufficient .

