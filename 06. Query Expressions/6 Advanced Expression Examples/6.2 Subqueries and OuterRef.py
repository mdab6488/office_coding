# Subqueries with OuterRef allow you to reference fields from the outer query in subqueries 

from django.db.models import OuterRef, Subquery, Exists

# Using Exists with subquery
non_unique_account_type = Client.objects.filter(
    account_type=OuterRef('account_type'),
).exclude(pk=OuterRef('pk')).values('pk')

Client.objects.filter(~Exists(non_unique_account_type))

# Using Subquery to annotate with related data
latest_comment = Comment.objects.filter(
    product=OuterRef('pk')
).order_by('-created_at').values('text')[:1]

Product.objects.annotate(
    latest_comment_text=Subquery(latest_comment)
)