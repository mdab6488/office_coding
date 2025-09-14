# Django models have default equality comparison based on primary key:

article1 = Article.objects.get(pk=1)
article2 = Article.objects.get(pk=1)
article3 = Article.objects.get(pk=2)

print(article1 == article2)  # Output: True (same primary key)
print(article1 == article3)  # Output: False (different primary keys)