# When using conditional expressions, following best practices ensures optimal performance and maintainable code.

"""
Database Compatibility: Be aware that Django implements conditional aggregation differently across database engines. On supported databases, the FILTER clause is used, while others use CASE statements .

Indexing: Ensure fields used in conditional expressions are properly indexed, especially for frequently used filters.

Select Related: When working with related models, use select_related() or prefetch_related() to minimize database queries.
"""
# Efficient query with select_related
agreements = Agreement.objects.filter(
    organization=self.organization
).select_related(
    'signed_agreement'
).annotate(
    signed=Case(
        When(signed_agreement__member_id=self.member.pk, then=Value(True)),
        default=Value(False),
        output_field=BooleanField()
    )
)

