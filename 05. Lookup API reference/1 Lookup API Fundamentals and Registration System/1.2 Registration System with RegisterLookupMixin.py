# Django uses the RegisterLookupMixin class to provide lookup registration capabilities. This mixin enables classes to register lookups either at the class level or instance level:

from django.db.models import Field, Lookup

# Register a lookup at the field class level
Field.register_lookup(MyCustomLookup)

# Register a lookup on a specific field instance
from myapp.models import MyModel
field_instance = MyModel._meta.get_field("field_name")
field_instance.register_lookup(MyInstanceSpecificLookup)

# The registration system follows a precedence hierarchy where lookups registered on field instances take priority over those registered at the class level, allowing for flexible override capabilities.

