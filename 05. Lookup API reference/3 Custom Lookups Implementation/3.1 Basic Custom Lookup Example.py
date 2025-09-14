# Creating custom lookups extends Django's query capabilities to handle specialized filtering requirements not covered by built-in lookups.

# Implementing a not equal lookup demonstrates the fundamental process:

from django.db.models import Lookup, Field

class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params

# Register the lookup
Field.register_lookup(NotEqual)

# This custom lookup can then be used in queries:

# Find all products not named "Laptop"
Product.objects.filter(name__ne='Laptop')

# The as_sql method is where the SQL generation logic resides. The process_lhs and process_rhs methods handle the left-hand and right-hand side processing respectively.

