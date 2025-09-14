# Sometimes different database backends require vendor-specific SQL:

from django.db.models import Lookup

class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        
        # Use != for MySQL, <> for other databases
        if connection.vendor == 'mysql':
            return '%s != %s' % (lhs, rhs), params
        else:
            return '%s <> %s' % (lhs, rhs), params
        
# This approach allows for database-aware SQL generation, accommodating syntax differences between database vendors.

