# You can combine Q objects with F expressions to create powerful filtering conditions based on field comparisons 

# Find products where price is greater than discounted price AND stock is low
Product.objects.filter(
    Q(price__gt=F('discounted_price')) & 
    Q(stock__lt=10)
)

# Find users whose last login was more than 30 days after registration
User.objects.filter(
    Q(last_login__gt=F('date_joined') + timedelta(days=30))
)

# Complex combined expression
Product.objects.filter(
    Q(price__gt=F('cost_price') * 2) |
    Q(Q(stock__lt=5) & Q(discontinued=False))
)