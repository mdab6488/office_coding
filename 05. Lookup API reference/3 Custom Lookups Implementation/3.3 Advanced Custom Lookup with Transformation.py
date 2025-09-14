# Custom lookups can also incorporate value transformations:

from django.db.models import Lookup

class AbsoluteValueLessThan(Lookup):
    lookup_name = 'lt'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = compiler.compile(self.lhs.lhs)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params + lhs_params + rhs_params
        return '%s < %s AND %s > -%s' % (lhs, rhs, lhs, rhs), params
    
# This lookup efficiently handles absolute value comparisons by generating a range query that can leverage database indexes:
# Find experiments where absolute change is less than 27
Experiment.objects.filter(change__abs__lt=27)

# The generated SQL would be:
# WHERE "experiments"."change" < 27 AND "experiments"."change" > -27

# This approach is more performance-optimized than applying the ABS() function to the column, as it allows index usage

