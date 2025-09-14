from datetime import date, timedelta

# Segment customers based on registration date and account type
a_month_ago = date.today() - timedelta(days=30)
a_year_ago = date.today() - timedelta(days=365)

segments = Client.objects.annotate(
    segment=Case(
        When(account_type=Client.PLATINUM, then=Value('premium')),
        When(account_type=Client.GOLD, 
             registered_on__lte=a_year_ago, 
             then=Value('loyal_gold')),
        When(account_type=Client.GOLD, then=Value('new_gold')),
        When(registered_on__lte=a_year_ago, then=Value('legacy')),
        When(registered_on__lte=a_month_ago, then=Value('recent')),
        default=Value('new')
    )
)

# Customer segmentation is a common use case for conditional expressions, enabling targeted marketing and personalized user experiences 