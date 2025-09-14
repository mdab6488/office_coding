# Creating a custom transform for absolute values:

from django.db.models import Transform

class AbsoluteValue(Transform):
    lookup_name = 'abs'
    function = 'ABS'

    @property
    def output_field(self):
        from django.db.models import FloatField
        return FloatField()

# Register for IntegerField
from django.db.models import IntegerField
IntegerField.register_lookup(AbsoluteValue)

# This transform can be chained with lookups:
# Find experiments with absolute change exactly equal to 27
Experiment.objects.filter(change__abs=27)

# Find experiments with absolute change less than 27
Experiment.objects.filter(change__abs__lt=27)

# Use in ordering
Experiment.objects.order_by('change__abs')

# The output_field property informs Django about the result type of the transformation, ensuring subsequent lookups are appropriate for the transformed value
