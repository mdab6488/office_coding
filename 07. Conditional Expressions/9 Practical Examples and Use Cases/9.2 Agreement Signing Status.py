from django.db.models import BooleanField, Case, When, Value

# Annotate agreements with signing status for a specific member
agreements = Agreement.objects.filter(
    organization=self.organization
).annotate(
    signed=Case(
        When(signed_agreement__member_id=self.member.pk, then=Value(True)),
        default=Value(False),
        output_field=BooleanField()
    )
).order_by('name')

# This pattern is useful for tracking user-specific status information in multi-user applications .

