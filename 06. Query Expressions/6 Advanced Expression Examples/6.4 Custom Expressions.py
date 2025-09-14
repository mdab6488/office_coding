# For database-specific functionality, you can create custom expressions when built-in options are insufficient 

from django.db.models import Func, F, Value

# Example of a custom expression
class Round(Func):
    function = 'ROUND'
    arity = 2  # Number of arguments

# Using the custom expression
Product.objects.annotate(
    rounded_price=Round(F('price'), 0)
)

# Another example with database-specific function
class DateDiff(Func):
    function = 'DATEDIFF'
    template = '%(function)s(day, %(expressions)s)'

Order.objects.annotate(
    days_since_order=DateDiff(Value(date.today()), F('order_date'))
)