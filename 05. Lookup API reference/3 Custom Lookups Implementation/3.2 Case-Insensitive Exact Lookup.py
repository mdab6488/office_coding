# For databases where case-insensitive matching isn't natively supported, a custom case-insensitive lookup can be implemented:

from django.db.models import Lookup
from django.db.models.functions import Lower

class CaseInsensitiveExact(Lookup):
    lookup_name = 'iexact'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return 'LOWER(%s) = LOWER(%s)' % (lhs, rhs), params

# Register for CharField and TextField
from django.db.models import CharField, TextField
CharField.register_lookup(CaseInsensitiveExact)
TextField.register_lookup(CaseInsensitiveExact)

# This implementation uses the SQL LOWER() function to normalize case for both sides of the comparison