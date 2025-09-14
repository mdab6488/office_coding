# For better performance with absolute value queries, especially on large datasets, a range-based approach can be implemented:

from django.db.models import Lookup

class AbsoluteValueLessThan(Lookup):
    lookup_name = 'lt'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = compiler.compile(self.lhs.lhs)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params + lhs_params + rhs_params
        return '%s < %s AND %s > -%s' % (lhs, rhs, lhs, rhs), params

# Register the lookup with the AbsoluteValue transform
AbsoluteValue.register_lookup(AbsoluteValueLessThan)

# This implementation bypasses the transform for index-friendly queries:

# Uses range query instead of ABS() function
Experiment.objects.filter(change__abs__lt=27)

# The generated SQL can utilize indexes on the "change" column:
WHERE "experiments"."change" < 27 AND "experiments"."change" > -27


# This optimization demonstrates how understanding database performance characteristics can inform custom lookup implementation
