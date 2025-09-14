# You can exclude certain fields from validation:

# Validate all fields except 'pub_date'
try:
    article.full_clean(exclude=['pub_date'])
except ValidationError as e:
    print(e.message_dict)